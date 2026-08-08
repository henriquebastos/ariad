#!/usr/bin/env python3
"""Strictly read-only structural audit against an explicit Ariad checkout."""
from __future__ import annotations

import argparse, hashlib, json, os, re, stat, subprocess
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, urlunsplit

MARKER = "<!-- ariad-entrypoint: docs/ariad/index.md -->"
DIRECTIVE = "@docs/ariad/index.md"
OLD_MARKER = "<!-- ariad-skill: using-ariad -->"
SKILL_LOCATIONS = (".agents/skills/using-ariad", ".claude/skills/using-ariad", ".codex/skills/using-ariad", "skills/using-ariad")
HARNESSES = ("AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursorrules", ".github/copilot-instructions.md")
HARNESS_SUPPORT = (".agents/setup", ".agents/resume", ".amp/services.yaml")
MEMORY_NAMES = ("decisions", "roadmap", "exploration", "debt", "worklog", "workbench")
LEGACY = {"briefing": "docs/project/briefing.md", "development_guide": "docs/process/development-guide.md", "principles": "docs/product/principles.md"}
MODULAR = {k: v.removesuffix(".md") + "/index.md" for k, v in LEGACY.items()}
DOC_ROOTS = ("docs/process", "docs/project", "docs/product", "docs/references", "docs/operator")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
TARGET_EXCLUDES = {".git", ".venv", "node_modules", "site", "build", "dist", ".agents", ".claude", ".codex"}
TEXT_EXCLUDES = {".git", ".venv", "node_modules", "site", "build", "dist"}
STATUS = re.compile(r"^\s*(?:[-*]\s*)?(?:\*\*)?status(?:\*\*)?\s*:\s*(.+?)\s*$", re.IGNORECASE)

def safe_relative(value: str) -> bool:
    return bool(value) and "\\" not in value and not PurePosixPath(value).is_absolute() and all(p not in ("", ".", "..") for p in value.split("/"))

def probe(boundary: Path, relative: str) -> tuple[str, Path | None]:
    """lstat each component below boundary; never traverse a collision."""
    if not safe_relative(relative): return "collision", None
    current = boundary
    for i, part in enumerate(relative.split("/")):
        current = current / part
        try: mode = current.lstat().st_mode
        except FileNotFoundError: return "absent", current
        except OSError: return "collision", None
        final = i == len(relative.split("/")) - 1
        if stat.S_ISLNK(mode) or (not final and not stat.S_ISDIR(mode)): return "collision", current
        if final:
            if stat.S_ISREG(mode): return "file", current
            if stat.S_ISDIR(mode): return "dir", current
            return "collision", current
    return "collision", None

def sanitize_url(value: str | None) -> str | None:
    if not value: return value
    scp = re.fullmatch(r"(?:(?P<user>[^/@:\s]+)@)?(?P<host>[^/@:\s]+):(?P<path>[^?#\s]+)(?:[?#].*)?", value) if "://" not in value else None
    if scp and (scp.group("user") or "." in scp.group("host")):
        m = scp
        return f"{m.group('host')}:{m.group('path')}"
    try: parsed = urlsplit(value)
    except ValueError: return "<redacted-unrecognized-url>"
    if parsed.scheme:
        if not parsed.netloc or parsed.hostname is None: return "<redacted-unrecognized-url>"
        try: port = parsed.port
        except ValueError: return "<redacted-unrecognized-url>"
        host = f"[{parsed.hostname}]" if ":" in parsed.hostname else parsed.hostname
        if port is not None: host += f":{port}"
        return urlunsplit((parsed.scheme, host, parsed.path, "", ""))
    if parsed.netloc or parsed.query or parsed.fragment or "@" in parsed.path or "://" in value:
        return "<redacted-unrecognized-url>"
    if parsed.path and not any(c in parsed.path for c in "\r\n"):
        return parsed.path
    return "<redacted-unrecognized-url>"

def git(root: Path, *args: str) -> str | None:
    env = os.environ.copy(); env["GIT_OPTIONAL_LOCKS"] = "0"
    try: result = subprocess.run(["git", "-C", str(root), *args], text=True, capture_output=True, env=env)
    except OSError: return None
    return result.stdout.strip() if result.returncode == 0 else None

def git_report(root: Path) -> dict:
    status, staged = git(root, "status", "--porcelain=v1"), git(root, "diff", "--cached", "--name-only")
    return {"branch": git(root, "branch", "--show-current"), "head": git(root, "rev-parse", "HEAD"),
            "dirty": None if status is None else bool(status), "staged": None if staged is None else bool(staged)}

def digest_bytes(data: bytes) -> str: return hashlib.sha256(data).hexdigest()

def package(root: Path, boundary: Path) -> dict:
    try: rel = root.relative_to(boundary).as_posix()
    except ValueError: rel = ""
    root_state, _ = probe(boundary, rel)
    result = {"path": root.as_posix(), "present": root_state == "dir", "manifest": None}
    reasons: list[str] = []
    if root_state != "dir":
        result["manifest"] = {"valid": False, "invalid_reasons": ["package root absent or unsafe"]}; return result
    state, manifest_path = probe(boundary, f"{rel}/manifest.json")
    if state != "file" or manifest_path is None:
        result["manifest"] = {"valid": False, "invalid_reasons": ["manifest missing or unsafe"]}; return result
    try: data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        result["manifest"] = {"valid": False, "invalid_reasons": ["unreadable manifest"]}; return result
    report = {"valid": False, "version": data.get("package_version") if isinstance(data, dict) else None,
              "method_digest": data.get("method_digest") if isinstance(data, dict) else None,
              "package_digest": data.get("package_digest") if isinstance(data, dict) else None, "invalid_reasons": reasons}
    required = (("format_version", "1"), ("package", "using-ariad"), ("source_path", "skills/using-ariad"))
    for key, expected in required:
        if not isinstance(data, dict) or data.get(key) != expected: reasons.append(f"invalid {key}")
    if not isinstance(report["version"], str) or not report["version"]: reasons.append("invalid package_version")
    for key in ("method_digest", "package_digest"):
        if not isinstance(report[key], str) or not SHA256.fullmatch(report[key]): reasons.append(f"invalid {key}")
    files = data.get("files") if isinstance(data, dict) else None
    if not isinstance(files, list): reasons.append("files inventory is not a list"); files = []
    destinations: set[str] = set(); payload: dict[str, bytes] = {}
    for item in files:
        destination = item.get("destination") if isinstance(item, dict) else None
        if not isinstance(destination, str) or not safe_relative(destination): reasons.append(f"invalid destination: {destination}"); continue
        if destination in destinations: reasons.append(f"duplicate destination: {destination}"); continue
        destinations.add(destination); expected_sha = item.get("sha256")
        if not isinstance(expected_sha, str) or not SHA256.fullmatch(expected_sha): reasons.append(f"invalid sha256: {destination}"); continue
        state, path = probe(boundary, f"{rel}/{destination}")
        if state != "file" or path is None: reasons.append(f"destination missing or unsafe: {destination}"); continue
        try: content = path.read_bytes()
        except OSError: reasons.append(f"destination unreadable: {destination}"); continue
        if digest_bytes(content) != expected_sha: reasons.append(f"sha256 mismatch: {destination}")
        payload[destination] = content
    if "SKILL.md" not in destinations: reasons.append("required SKILL.md missing from inventory")
    actual = inventory(root)
    expected = destinations | {"manifest.json"}
    for name in sorted(expected - actual): reasons.append(f"missing inventory file: {name}")
    for name in sorted(actual - expected): reasons.append(f"unexpected inventory file: {name}")
    calculated = digest_bytes(b"".join(n.encode()+b"\0"+payload[n]+b"\0" for n in sorted(payload)))
    if calculated != report["package_digest"]: reasons.append("package digest mismatch")
    report["valid"] = not reasons; result["manifest"] = report; return result

def inventory(root: Path) -> set[str]:
    """Inventory every file and symlink entry without following symlink directories."""
    found: set[str] = set()
    for directory, dirnames, filenames in os.walk(root, followlinks=False):
        base = Path(directory)
        for name in list(dirnames):
            path = base / name
            if path.is_symlink():
                found.add(path.relative_to(root).as_posix())
                dirnames.remove(name)
        found.update((base / name).relative_to(root).as_posix() for name in filenames)
    return found

def safe_files(root: Path, pattern: str, excluded: set[str] | None = None) -> list[Path]:
    found=[]
    excluded = excluded or {".git"}
    for directory, dirnames, filenames in os.walk(root, followlinks=False):
        base=Path(directory); dirnames[:]=sorted(d for d in dirnames if d not in excluded and not (base/d).is_symlink())
        found.extend(base/n for n in sorted(filenames) if not (base/n).is_symlink() and (pattern == "*" or (base/n).match(pattern)))
    return found

def target_text_files(root: Path) -> list[Path]:
    """Return bounded project text candidates without following links or vendored skills."""
    found=[]
    for path in safe_files(root,"*",TEXT_EXCLUDES):
        relative=path.relative_to(root).as_posix()
        if any(relative.startswith(prefix) for prefix in (".agents/skills/", ".claude/skills/", ".codex/skills/")): continue
        try:
            if path.stat().st_size <= 2_000_000 and b"\0" not in path.read_bytes()[:8192]: found.append(path)
        except OSError: continue
    return found

def memory_summary(target: Path, memories: list[str]) -> list[dict]:
    summaries=[]
    for relative in memories:
        state,root=probe(target,relative)
        files=safe_files(root,"*.md",set()) if state == "dir" and root else []
        statuses=set()
        for path in files:
            try: lines=path.read_text(encoding="utf-8",errors="replace").splitlines()
            except OSError: continue
            for line in lines:
                match=STATUS.match(line)
                if match:
                    value=match.group(1).strip().strip("*_`").strip()
                    if value: statuses.add(value)
        entries=[p for p in files if p.name.lower() not in ("index.md","readme.md")]
        summaries.append({"path":relative,"markdown_files":len(files),"entries":len(entries),"statuses":sorted(statuses)})
    return summaries

def contract(boundary: Path, relative: str) -> dict:
    state, path = probe(boundary, relative); lines=[]
    if state == "file" and path:
        try: lines=path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError: state="collision"
    return {"path": relative, "state": state, "present": state == "file", "marker": lines.count(MARKER)==1, "directive": lines.count(DIRECTIVE)==1}

def manifest_delta(old: dict, new: dict) -> dict:
    def inventory(pkg): return {x["destination"]: x["sha256"] for x in json.loads((Path(pkg["path"])/"manifest.json").read_text())["files"]}
    a,b=inventory(old),inventory(new)
    return {"added": sorted(b.keys()-a.keys()), "removed": sorted(a.keys()-b.keys()), "changed": sorted(k for k in a.keys()&b.keys() if a[k]!=b[k])}

def audit(target: Path, candidate: Path, installed_paths: list[str] | None=None, destination: str | None=None) -> dict:
    installed_paths=installed_paths or []
    agents=sorted(p.relative_to(target).as_posix() for p in safe_files(target,"AGENTS.md",TARGET_EXCLUDES)); root=contract(target,"AGENTS.md")
    locations=[]
    for rel in (*SKILL_LOCATIONS,*installed_paths):
        if rel not in locations and probe(target,rel)[0] in ("dir","collision"): locations.append(rel)
    installed=[package(target/rel,target) for rel in locations]
    candidate_pkg=package(candidate/"skills/using-ariad",candidate); cm=candidate_pkg.get("manifest") or {}
    components={"source_template":contract(candidate,"docs/project-templates/AGENTS.md"), "packaged_agents_asset":contract(candidate,"skills/using-ariad/assets/project-templates/AGENTS.md"),
                "source_router":probe(candidate,"docs/project-templates/docs/ariad/index.md")[0]=="file", "packaged_router":probe(candidate,"skills/using-ariad/assets/project-templates/docs/ariad/index.md")[0]=="file"}
    compatible=all((components["source_template"]["marker"],components["source_template"]["directive"],components["packaged_agents_asset"]["marker"],components["packaged_agents_asset"]["directive"],components["source_router"],components["packaged_router"]))
    eligible=bool(cm.get("valid") and compatible)
    refs={v:[] for v in LEGACY.values()}
    docs_state, docs_root = probe(target,"docs")
    markdown = safe_files(docs_root,"*.md",set()) if docs_state == "dir" and docs_root else []
    text_files=target_text_files(target)
    semantic_evidence=[]
    for source in text_files:
        try: text=source.read_text(encoding="utf-8",errors="replace")
        except OSError: continue
        relative=source.relative_to(target).as_posix()
        for legacy in refs:
            if legacy in text and relative != legacy: refs[legacy].append(relative)
        lowered=text.lower()
        if "ariad" in lowered and any(term in lowered for term in ("canonical", "driver", "navigator", "hermes", "method")):
            semantic_evidence.append(relative)
    memories=set()
    memory_root = docs_root if docs_state == "dir" and docs_root else None
    for directory, dirnames, _ in os.walk(memory_root, followlinks=False) if memory_root else []:
        base=Path(directory); dirnames[:]=[d for d in dirnames if d != ".git" and not (base/d).is_symlink()]
        for name in dirnames:
            if name.lower() in MEMORY_NAMES: memories.add((base/name).relative_to(target).as_posix())
    memories=sorted(memories)
    summaries=memory_summary(target,memories)
    memory_prefixes=tuple(path+"/" for path in memories)
    focused=sorted(p.relative_to(target).as_posix() for p in markdown if any(p.relative_to(target).as_posix().startswith(r+"/") for r in DOC_ROOTS) and p.relative_to(target).as_posix() not in LEGACY.values() and not p.relative_to(target).as_posix().startswith(memory_prefixes))
    adjacent=[]
    for relative in ("README.md", "CONTEXT.md", "spec"):
        state,path=probe(target,relative)
        if state == "file": adjacent.append(relative)
        elif state == "dir" and path:
            adjacent.extend(p.relative_to(target).as_posix() for p in safe_files(path,"*.md",set()))
    adjacent=sorted(set(focused+adjacent))
    harness_support=[p for p in HARNESS_SUPPORT if probe(target,p)[0]=="file"]
    router=probe(target,"docs/ariad/index.md")[0]=="file"; old=False
    if root["present"]:
        _,rp=probe(target,"AGENTS.md"); old=OLD_MARKER in rp.read_text(encoding="utf-8",errors="replace").splitlines() if rp else False
    integration={"root_agents_present":root["present"],"root_agents_state":root["state"],"marker":root["marker"],"directive":root["directive"],"old_marker":old,"router":router,"router_state":probe(target,"docs/ariad/index.md")[0]}
    ops={"safe_additive":[],"manual_integration":[],"destructive_ambiguous_denied":[],"retain_unchanged":sorted(set(memories+adjacent+harness_support+[p for p in MODULAR.values() if probe(target,p)[0]=="file"]))}
    if not eligible: ops["destructive_ambiguous_denied"].append("candidate package or integration contract invalid; candidate-derived automation denied")
    if installed:
        for p in installed: ops["manual_integration"].append(f"review existing package at {p['path']}; replacement is manual")
    elif destination is None: ops["manual_integration"].append("no package found in probed locations; select installation destination manually")
    elif eligible:
        state,_=probe(target,destination)
        (ops["safe_additive"] if state=="absent" else ops["manual_integration"]).append(("install complete using-ariad package at " if state=="absent" else "destination is not proven absent: ")+destination)
    if root["state"]=="absent" and eligible: ops["safe_additive"].append("add minimal root AGENTS.md entrypoint")
    elif root["present"] and not(root["marker"] and root["directive"]): ops["manual_integration"].append("add exact entrypoint block to project-owned AGENTS.md")
    elif root["state"]=="collision": ops["manual_integration"].append("root AGENTS.md path is unsafe or colliding")
    if old: ops["manual_integration"].append("replace incompatible legacy Ariad integration block")
    existing=bool(memories or old or any(probe(target,p)[0] != "absent" for p in (*LEGACY.values(),*MODULAR.values(),*DOC_ROOTS)))
    if not router and integration["router_state"]=="absent" and eligible: ops["manual_integration" if existing else "safe_additive"].append("add docs/ariad/index.md router")
    elif integration["router_state"]=="collision": ops["manual_integration"].append("docs/ariad/index.md path is unsafe or colliding")
    for path in LEGACY.values():
        if probe(target,path)[0] != "absent": ops["destructive_ambiguous_denied"].append(f"retain; semantic migration of {path} is manual")
    deltas=[]
    if cm.get("valid"):
        for p in installed:
            if (p.get("manifest") or {}).get("valid"):
                try: deltas.append({"path":p["path"],**manifest_delta(p,candidate_pkg)})
                except (OSError,ValueError,KeyError): pass
    cg=git_report(candidate)
    candidate_report={"path":str(candidate),"source_url":sanitize_url(git(candidate,"config","--get","remote.origin.url")),"revision":cg["head"],"branch":cg["branch"],"dirty":cg["dirty"],"staged":cg["staged"],"version":cm.get("version"),"method_digest":cm.get("method_digest"),"package_digest":cm.get("package_digest"),"package_valid":cm.get("valid",False),"package_invalid_reasons":cm.get("invalid_reasons",[]),"contract_components":components,"contract_compatible":compatible,"using_ariad":candidate_pkg}
    absences={"exploration_memory":not any(p.endswith("/exploration") or p == "exploration" for p in memories),
              "empty_worklog":any(s["path"].endswith("/worklog") and s["entries"] == 0 for s in summaries)}
    return {"schema_version":1,"mode":"report-only","target":str(target),"git":git_report(target),"agents_scopes":agents,"harness_files":[p for p in HARNESSES if probe(target,p)[0]=="file"],"harness_support_files":harness_support,"integration":integration,"installed_packages":installed,"candidate":candidate_report,"candidate_compatibility":components,"candidate_compatible":compatible,"package_deltas":deltas,"documents":{k:{"legacy":probe(target,LEGACY[k])[0]=="file","modular_index":probe(target,MODULAR[k])[0]=="file"} for k in LEGACY},"legacy_inbound_references":refs,"semantic_ariad_evidence":sorted(set(semantic_evidence)),"project_memory":memories,"project_memory_summary":summaries,"intentional_absence_candidates":absences,"adjacent_project_docs":adjacent,"operations":ops}

def show(v): return "unknown" if v is None else str(v)
def render(data: dict) -> str:
    c=data["candidate"]
    documents="; ".join(f"{name}=legacy:{state['legacy']},modular:{state['modular_index']}" for name,state in data["documents"].items())
    inbound=[f"{path} <- {', '.join(refs)}" for path,refs in data["legacy_inbound_references"].items() if refs]
    components=c["contract_components"]
    memory="; ".join(f"{s['path']} ({s['entries']} entries, statuses: {', '.join(s['statuses']) or 'none'})" for s in data["project_memory_summary"])
    absence=data["intentional_absence_candidates"]
    evidence=data["semantic_ariad_evidence"]
    evidence_summary=(f"{len(evidence)} paths (examples: {', '.join(evidence[:5])}; full inventory in JSON)" if evidence else "none")
    lines=["Ariad upgrade audit (report-only)",f"Target: {data['target']}",f"Git: branch={show(data['git']['branch'])} head={show(data['git']['head'])} dirty={show(data['git']['dirty'])} staged={show(data['git']['staged'])}",f"Candidate: source={show(c['source_url'])} revision={show(c['revision'])} branch={show(c['branch'])} dirty={show(c['dirty'])} staged={show(c['staged'])}",f"  version={show(c['version'])} method={show(c['method_digest'])} package={show(c['package_digest'])} valid={c['package_valid']} contract={c['contract_compatible']} reasons={'; '.join(c['package_invalid_reasons']) or 'none'}",f"  contract components: source-template={components['source_template']['marker'] and components['source_template']['directive']} packaged-agents={components['packaged_agents_asset']['marker'] and components['packaged_agents_asset']['directive']} source-router={components['source_router']} packaged-router={components['packaged_router']}",f"AGENTS scopes: {', '.join(data['agents_scopes']) or 'none'}",f"Harness files: {', '.join(data['harness_files']) or 'none'}",f"Harness support (retain): {', '.join(data['harness_support_files']) or 'none'}",f"Entrypoint: marker={data['integration']['marker']} directive={data['integration']['directive']} router={data['integration']['router']} old-marker={data['integration']['old_marker']}",f"Documents: {documents}","Legacy inbound references: "+("; ".join(inbound) or "none"),f"Semantic Ariad evidence: {evidence_summary}",f"Project memory: {memory or 'none'}",f"Possible intentional absences: exploration={absence['exploration_memory']} empty-worklog={absence['empty_worklog']}",f"Adjacent project docs: {len(data['adjacent_project_docs'])} (full inventory in JSON)"]
    if not data["installed_packages"]: lines.append("Installed packages: none")
    for p in data["installed_packages"]:
        m=p.get("manifest") or {}; lines.append(f"Installed: {p['path']} version={show(m.get('version'))} method={show(m.get('method_digest'))} package={show(m.get('package_digest'))} valid={m.get('valid',False)} reasons={'; '.join(m.get('invalid_reasons',[])) or 'none'}")
    for d in data["package_deltas"]: lines.append(f"Delta {d['path']}: added={d['added']} removed={d['removed']} changed={d['changed']}")
    for kind,values in data["operations"].items(): lines.append(f"{kind.replace('_',' ').title()}: "+("; ".join(values) or "none"))
    return "\n".join(lines)+"\n"

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("target",type=Path); parser.add_argument("--candidate",required=True,type=Path); parser.add_argument("--installed-package",action="append",default=[]); parser.add_argument("--skill-destination"); parser.add_argument("--json",action="store_true"); args=parser.parse_args()
    for value in [*args.installed_package,*([args.skill_destination] if args.skill_destination else [])]:
        if not safe_relative(value): parser.error("package paths must be safe target-relative paths")
    target,candidate=args.target.expanduser().resolve(),args.candidate.expanduser().resolve()
    if not target.is_dir() or not candidate.is_dir(): parser.error("target and candidate must be existing directories")
    data=audit(target,candidate,args.installed_package,args.skill_destination); print(json.dumps(data,indent=2,sort_keys=True) if args.json else render(data),end="\n" if args.json else ""); return 0
if __name__=="__main__": raise SystemExit(main())

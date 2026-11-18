#!/usr/bin/env python3
"""Pre-push check for this repo. Run from anywhere: python3 scripts/check.py

1. Lists installed skills, plugins, hooks, MCP servers and command-line tools,
   and flags any that the kit never mentions.
2. Prints a known-good version table (Markdown) for examples/copy-me-exactly.md.
3. Scans the repo for IP addresses, email addresses and token patterns.

Exits 1 if the scan finds anything, so it can gate a push.
Collaborators' names, student data and life admin can't be matched by a pattern:
read the diff for those.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HOME = Path.home()
CLAUDE = HOME / ".claude"
CLIS = ["claude", "rtk", "herdr", "graphify"]

SCRUB = {
    "IP address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "email": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
    "token": re.compile(
        r"ghp_\w{20,}|github_pat_\w{20,}|sk-ant-[\w-]{20,}|sk-[A-Za-z0-9]{32,}"
        r"|AKIA[0-9A-Z]{16}|xox[bp]-[\w-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----"
    ),
}
# Placeholders that look like matches but aren't private.
ALLOWED = {"noreply@github.com", "git@github.com", "you@example.com"}


def load_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return {}


def installed():
    """Return {group: [names]} for everything on this machine."""
    settings = load_json(CLAUDE / "settings.json")
    skills = sorted(p.name for p in (CLAUDE / "skills").iterdir()
                    if (p / "SKILL.md").exists()) if (CLAUDE / "skills").exists() else []
    plugins = sorted(k.split("@")[0] for k, on in settings.get("enabledPlugins", {}).items() if on)
    hooks = sorted({h["command"].split()[0] if not h["command"].startswith("bash ")
                    else Path(h["command"].split()[1].strip("'\"")).stem
                    for event in settings.get("hooks", {}).values()
                    for entry in event for h in entry.get("hooks", [])})
    mcp = sorted(load_json(HOME / ".claude.json").get("mcpServers", {}))
    return {"skills": skills, "plugins": plugins, "hooks": hooks, "MCP servers": mcp, "CLI": CLIS}


def version(cli):
    try:
        out = subprocess.run([cli, "--version"], capture_output=True, text=True, timeout=20).stdout
    except (OSError, subprocess.TimeoutExpired):
        return None
    m = re.search(r"\d+\.\d+[\w.]*", out)
    return m.group(0) if m else None


def version_table():
    rows = [(c, version(c)) for c in CLIS]
    plugins = load_json(CLAUDE / "plugins" / "installed_plugins.json").get("plugins", {})
    rows += [(k.split("@")[0], v[0].get("version")) for k, v in plugins.items() if v]
    lines = ["| Tool | Version |", "| --- | --- |"]
    lines += [f"| {name} | {ver or 'not installed'} |" for name, ver in rows]
    return "\n".join(lines)


def kit_text():
    return "\n".join(p.read_text(encoding="utf-8") for p in (REPO / "kit").glob("*.md")).lower()


def scrub():
    files = subprocess.run(["git", "-C", str(REPO), "ls-files", "-co", "--exclude-standard"],
                           capture_output=True, text=True, check=True).stdout.split()
    hits = []
    for rel in files:
        if rel == "scripts/check.py":
            continue
        try:
            text = (REPO / rel).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue  # binary (images)
        for n, line in enumerate(text.splitlines(), 1):
            for kind, rx in SCRUB.items():
                for m in rx.finditer(line):
                    if m.group(0) not in ALLOWED:
                        hits.append(f"{rel}:{n}: {kind}: {m.group(0)}")
    return hits


def main():
    kit = kit_text()
    print("== Installed, and missing from kit/ ==")
    for group, names in installed().items():
        missing = [n for n in names if n.lower() not in kit]
        print(f"{group}: {len(names)} installed" + (f", missing: {', '.join(missing)}" if missing else ""))

    print("\n== Known-good versions ==")
    print(version_table())

    print("\n== Scrub scan ==")
    hits = scrub()
    print("\n".join(hits) if hits else "clean")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()

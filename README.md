# Atlas Go Skill

Atlas Go is a Codex/Claude-compatible learning skill that turns requests like "teach me X" into durable, high-quality lesson pages backed by a breadth-first knowledge map.

## Project Structure

- `atlas-go/.claude/skills/atlas-go/SKILL.md` - skill entrypoint
- `atlas-go/.claude/skills/atlas-go/references/` - required reference docs used by the skill
- `atlas-go/atlas-go.json` - map + memory of topics, progress, and links
- `atlas-go/pages/` - generated lesson pages
- `atlas-go/scripts/build_index.py` - regenerates `atlas-go/index.html` from `atlas-go.json`
- `atlas-go/assets/atlas-go.css` - visual design system

## Global Installation (Codex)

This repo includes the skill at:

`atlas-go/.claude/skills/atlas-go`

To install globally:

```bash
mkdir -p ~/.codex/skills
cp -R atlas-go/.claude/skills/atlas-go ~/.codex/skills/atlas-go
```

Restart Codex after installation.

## Local Usage

From the `atlas-go/` directory:

```bash
python3 scripts/build_index.py
```

This rebuilds `index.html` from `atlas-go.json`.

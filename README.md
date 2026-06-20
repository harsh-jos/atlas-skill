# Atlas Skill

Atlas is a Codex/Claude-compatible learning skill that turns requests like "teach me X" into durable, high-quality lesson pages backed by a breadth-first knowledge map.

## Project Structure

- `atlas/.claude/skills/atlas/` - installable skill bundle (`SKILL.md` + references)
- `atlas/atlas.json` - map + memory of topics, progress, and links
- `atlas/pages/` - generated lesson pages
- `atlas/scripts/build_index.py` - regenerates `atlas/index.html` from `atlas.json`
- `atlas/assets/atlas.css` - visual design system

## Global Installation (Codex)

This repo includes the skill at:

`atlas/.claude/skills/atlas`

To install globally:

```bash
mkdir -p ~/.codex/skills
cp -R atlas/.claude/skills/atlas ~/.codex/skills/atlas
```

Restart Codex after installation.

## Local Usage

From the `atlas/` directory:

```bash
python3 scripts/build_index.py
```

This rebuilds `index.html` from `atlas.json`.

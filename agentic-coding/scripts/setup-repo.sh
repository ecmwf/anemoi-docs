#!/usr/bin/env bash

# 1. Create all root and config directories
mkdir -p .agents/commands
mkdir -p .agents/skills/example-skill
mkdir -p .agents/plugins
mkdir -p .claude
mkdir -p .cursor
mkdir -p .opencode
mkdir -p .github/prompts
mkdir -p .vscode
mkdir -p scripts/ai

# 2. Add .gitkeep to directories that might remain empty
touch .agents/commands/.gitkeep
touch .agents/plugins/.gitkeep
touch .github/prompts/.gitkeep
touch scripts/ai/.gitkeep

# 3. Touch primary source-of-truth configuration files
touch AGENTS.md
touch opencode.json
touch .agents/skills/example-skill/SKILL.md
touch .agents/commands/review.md
touch .agents/plugins/mcp-server.json

# 4. Create Root-Level Instruction Symlinks (Point to AGENTS.md)
ln -sf AGENTS.md CLAUDE.md
ln -sf AGENTS.md .cursorrules
ln -sf AGENTS.md .copilot-instructions.md

# 5. Link Claude Code harness paths to .agents standard
ln -sf ../.agents/commands .claude/commands
ln -sf ../.agents/skills .claude/skills

# 6. Link Cursor harness paths to .agents standard
ln -sf ../.agents/commands .cursor/commands
ln -sf ../.agents/skills .cursor/skills

# 7. Link OpenCode harness paths to .agents standard
ln -sf ../.agents/commands .opencode/commands
ln -sf ../.agents/skills .opencode/skills

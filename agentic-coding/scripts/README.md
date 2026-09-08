Run the `setup-repo.sh` script to create various files and directories used by various coding agents:

```
my-project/
├── AGENTS.md                     <-- Master instructions
├── CLAUDE.md                     -> Symlink to AGENTS.md
├── .cursorrules                  -> Symlink to AGENTS.md
├── .copilot-instructions.md      -> Symlink to AGENTS.md
├── opencode.json
│
├── .agents/                      <-- Canonical definitions
│   ├── commands/
│   │   └── review.md
│   ├── skills/
│   │   └── example-skill/
│   │       └── SKILL.md
│   └── plugins/
│       └── mcp-server.json
│
├── .claude/
│   ├── commands                   -> Symlink to ../.agents/commands
│   └── skills                     -> Symlink to ../.agents/skills
│
├── .cursor/
│   ├── commands                   -> Symlink to ../.agents/commands
│   └── skills                     -> Symlink to ../.agents/skills
│
└── .opencode/
    ├── commands                   -> Symlink to ../.agents/commands
    └── skills                     -> Symlink to ../.agents/skills
```

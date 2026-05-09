---
name: gsd
description: Get Shit Done (GSD) - Metodologia de planejamento e execução hierárquica.
---

# GSD Command Reference

**GSD** (Get Shit Done) creates hierarchical project plans optimized for solo agentic development with Claude Code.

## Quick Start

1. `/gsd-new-project` - Initialize project (includes research, requirements, roadmap)
2. `/gsd-plan-phase 1` - Create detailed plan for first phase
3. `/gsd-execute-phase 1` - Execute the phase

## Core Workflow

```
/gsd-new-project → /gsd-plan-phase → /gsd-execute-phase → repeat
```

### Project Initialization

**`/gsd-new-project`**
Initialize new project through unified flow.
Creates all `.planning/` artifacts: `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `config.json`.

**`/gsd-map-codebase`**
Map an existing codebase for brownfield projects. Creates `.planning/codebase/`.

### Phase Planning

**`/gsd-plan-phase <number>`**
Create detailed execution plan for a specific phase. Generates `PLAN.md`.

### Execution

**`/gsd-execute-phase <phase-number>`**
Execute all plans in a phase. Updates requirements, roadmap and state.

### Quick Mode

**`/gsd-quick`**
Execute small, ad-hoc tasks with GSD guarantees.

**`/gsd-fast [description]`**
Execute a trivial task inline — no subagents, no planning files.

### Progress Tracking

**`/gsd-progress`**
Check project status and intelligently route to next action.

**`/gsd-resume-work`** / **`/gsd-pause-work`**
Handoff and restoration of session context.

### Spiking & Sketching

**`/gsd-spike [idea]`** / **`/gsd-sketch [idea]`**
Rapidly validate feasibility or UI ideas with throwaway experiments/mockups.

---

*Note: For full documentation, refer to the original GSD workflow files.*

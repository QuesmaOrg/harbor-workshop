---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
color: #1a1a2e
style: |
  section {
    font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    padding: 40px 60px;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
  }
  h1 {
    color: #1a1a2e;
    font-weight: 700;
    border-bottom: 3px solid #4361ee;
    padding-bottom: 8px;
    display: inline-block;
  }
  h2 {
    color: #1a1a2e;
    font-weight: 700;
    margin-bottom: 24px;
  }
  h3 {
    color: #4361ee;
    font-weight: 600;
    margin-bottom: 12px;
  }
  code {
    background: #f0f1f6;
    color: #4361ee;
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 0.9em;
  }
  pre {
    background: #f8f9fc !important;
    border: 1px solid #e2e4ed;
    border-radius: 10px;
    padding: 20px !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }
  pre code {
    background: transparent;
    color: #2d3142;
    font-size: 0.85em;
  }
  strong {
    color: #e63946;
  }
  em {
    color: #7b2cbf;
    font-style: italic;
  }
  blockquote {
    border-left: 4px solid #4361ee;
    background: #f0f1f6;
    padding: 12px 20px;
    border-radius: 0 10px 10px 0;
    color: #555;
    font-size: 0.95em;
  }
  ul {
    line-height: 1.7;
  }
  section.lead {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.lead h1 {
    font-size: 2.4em;
    color: #1a1a2e;
    border-bottom: 4px solid #4361ee;
  }
  section.lead p {
    color: #6c757d;
    font-size: 1.15em;
    max-width: 700px;
  }
  section.lead pre {
    text-align: left;
  }
  .cols {
    display: flex;
    gap: 36px;
    align-items: flex-start;
  }
  .cols .tree {
    flex: 0 0 auto;
    font-size: 0.82em;
    line-height: 1.55;
  }
  .cols .tree pre {
    margin: 0;
    padding: 16px 20px !important;
    background: #f8f9fc !important;
  }
  .cols .desc {
    flex: 1;
  }
  .cols .desc h3 {
    margin-top: 0;
  }
  footer {
    color: #adb5bd;
    font-size: 0.7em;
  }
---

<!-- _class: lead -->

# Harbor Task Directory

How tasks are structured and what each piece does

---

## The Anatomy of a Task

```bash
└── example-task/
    ├── task.toml
    ├── instruction.md
    ├── environment
    │   ├── Dockerfile
    │   └── main.go
    ├── solution
    │   └── solve.sh
    └── tests
        └── test.sh
```

Convention: the directory name (`example-task`) is also the task name.

---

## `task.toml`

<div class="cols"><div class="tree">

```bash
└── example-task/
    ├── task.toml        ◄
    ├── instruction.md
    ├── environment/
    │   ├── Dockerfile
    │   └── main.go
    ├── solution/
    │   └── solve.sh
    └── tests/
        └── test.sh
```

</div><div class="desc">

### Task metadata

```toml
[metadata]
author_name = "Przemyslaw Hejman"
difficulty = "easy"
tags = ["trivial", "golang"]

[agent]
timeout_sec = 900.0

[environment]
cpus = 1
memory_mb = 4096
```

</div></div>

---

## `instruction.md`

<div class="cols"><div class="tree">

```bash
└── example-task/
    ├── task.toml
    ├── instruction.md   ◄
    ├── environment/
    │   ├── Dockerfile
    │   └── main.go
    ├── solution/
    │   └── solve.sh
    └── tests/
        └── test.sh
```

</div><div class="desc">

The prompt for LLM agent containing the actual assignment.

```md
You are expert Go programmer.
Your task is to compile Go program from source
code located in /app/src.
Succesful build should produce binary located
in /app/bin.
Fix any compilation errors and make sure the
binary runs successfully.
**DO NOT MODIFY** `/app/src/main.go` file.
```

</div></div>

---

## `environment/`

<div class="cols"><div class="tree">

```bash
└── example-task/
    ├── task.toml
    ├── instruction.md
    ├── environment/     ◄
    │   ├── Dockerfile   ◄
    │   └── main.go      ◄
    ├── solution/
    │   └── solve.sh
    └── tests/
        └── test.sh
```

</div><div class="desc">

### The world your task lives in

- `Dockerfile` — builds the container where the task runs
- Files required for the task — source code or anything which needs to be present in the container.
- _(optional)_ `docker-compose.yaml` to enforce _network isolation_ or bring up auxiliary containers.

</div></div>

---

## `tests/`

<div class="cols"><div class="tree">

```bash
└── example-task/
    ├── task.toml
    ├── instruction.md
    ├── environment/
    │   ├── Dockerfile
    │   └── main.go
    ├── solution/
    │   └── solve.sh
    └── tests/           ◄
        └── test.sh      ◄
```

</div><div class="desc">

### How we know the agent succeeded

- `test.sh` — test script which verifies that the agent completed the instruction.
  `tests/` directory gets copied and `tests/test.sh` is called.
  It is expected to procude a reward file in `/logs/verifier/reward.(txt|json)`

</div></div>

---

## `solution/`

<div class="cols"><div class="tree">

```bash
└── example-task/
    ├── task.toml
    ├── instruction.md
    ├── environment/
    │   ├── Dockerfile
    │   └── main.go
    ├── solution/        ◄
    │   └── solve.sh     ◄
    └── tests/
        └── test.sh
```

</div><div class="desc">

### Reference (oracle) solution

This is entirely _optional_, but may be required when submitting tasks to public benchmarks (e.g., TerminalBench).

Running `solve.sh` should make **all tests pass**.

</div></div>

---

## Running the example task

```bash
export OPENROUTER_API_KEY=...
```

```bash
harbor run -p "tasks/example-task" --agent terminus-2 --model openrouter/anthropic/claude-sonnet-4.5
```

Interactive preview of the task:

```bash
harbor view jobs/
```

---

## Agents

```bash
ANTHROPIC_API_KEY=sk-ant-api03-... \
harbor run -p "tasks/example-task" --agent claude-code
```

Multiple agents are available: `gemini-cli`, `codex`, ...

```bash
harbor run -p "tasks/example-task" --agent oracle
```

Special agent `oracle` for executing a reference solution.

---

## Environments

```bash
harbor run -p "tasks/example-task" --env daytona  --agent terminus-2 --model openrouter/anthropic/claude-sonnet-4.5
```

The default is a local Docker environment; to run tasks at scale, sandbox provider like Daytona can be used.
**Note:** this environment requires env `DAYTONA_API_KEY` being set.

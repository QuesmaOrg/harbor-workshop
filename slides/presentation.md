---
marp: true
theme: default
paginate: true
backgroundColor: #0d1117
color: #e6edf3
style: |
  section {
    font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
  }
  h1, h2 {
    color: #58a6ff;
  }
  h3 {
    color: #79c0ff;
  }
  code {
    background: #161b22;
    color: #79c0ff;
    border-radius: 4px;
    padding: 2px 6px;
  }
  pre {
    background: #161b22 !important;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 20px !important;
  }
  pre code {
    color: #e6edf3;
  }
  strong {
    color: #ff7b72;
  }
  em {
    color: #d2a8ff;
    font-style: normal;
  }
  blockquote {
    border-left: 4px solid #58a6ff;
    background: #161b22;
    padding: 12px 20px;
    border-radius: 0 8px 8px 0;
  }
  table {
    margin: 0 auto;
  }
  th {
    background: #161b22;
    color: #58a6ff;
  }
  td {
    background: #0d1117;
    border-color: #30363d;
  }
  section.lead h1 {
    font-size: 2.5em;
    color: #58a6ff;
  }
  section.lead p {
    color: #8b949e;
    font-size: 1.2em;
  }
  .cols {
    display: flex;
    gap: 40px;
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
  }
  .cols .desc {
    flex: 1;
  }
  .cols .desc h3 {
    margin-top: 0;
  }
  .hl {
    color: #ffa657;
    font-weight: bold;
  }
  .dim {
    opacity: 0.35;
  }
---

<!-- _class: lead -->

# Harbor Task Directory

How tasks are structured and what each piece does

---

## The Anatomy of a Task

```
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

```
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

```
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

```
You are expert Go programmer. 
Your task is to compile Go program from source code located in /app/src.
Succesful build should produce binary located in /app/bin.
Fix any compilation errors and make sure the binary runs successfully.
**DO NOT MODIFY** `/app/src/main.go` file.
```

</div></div>

---

## `environment/`

<div class="cols"><div class="tree">

```
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
- *(optional)* `docker-compose.yaml` to enforce *network isolation* or bring up auxiliary containers.

</div></div>

---

## `tests/`

<div class="cols"><div class="tree">

```
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

```
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

This is entirely *optional*, but may be required when submitting tasks to public benchmarks (e.g., TerminalBench).

Running `solve.sh` should make **all tests pass**.

</div></div>

---

<!-- _class: lead -->

# Running the example task

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

<!-- _class: lead -->

# Agents 

```bash
ANTHROPIC_API_KEY=sk-ant-api03-... \
harbor run -p "tasks/example-task" --agent claude-code
```

Multiple agents are available: `gemini-cli`, `codex`, ...
```
harbor run -p "tasks/example-task" --agent oracle
```
Special agent `oracle` for executing a reference solution. 


---

<!-- _class: lead -->

# Environments 

```bash
harbor run -p "tasks/example-task" --env daytona  --agent terminus-2 --model openrouter/anthropic/claude-sonnet-4.5
```

The default is a local Docker environment; to run tasks at scale, sandbox provider like Daytona can be used.
**Note:** this environment requires env `DAYTONA_API_KEY` being set. 
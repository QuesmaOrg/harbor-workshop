---
marp: true
theme: default
paginate: true
backgroundColor: #060d19
color: #e0e6ed
style: |
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
  section {
    font-family: 'Plus Jakarta Sans', 'Inter', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    padding: 40px 60px;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
  }
  h1 {
    color: #ffffff;
    font-weight: 700;
    border-bottom: 3px solid #20e0af;
    padding-bottom: 8px;
    display: inline-block;
  }
  h2 {
    color: #ffffff;
    font-weight: 700;
    margin-bottom: 24px;
  }
  h3 {
    color: #20e0af;
    font-weight: 600;
    margin-bottom: 12px;
  }
  code {
    background: #0f1d35;
    color: #20e0af;
    border-radius: 4px;
    padding: 2px 8px;
    font-size: 0.9em;
  }
  pre {
    background: #0a1424 !important;
    border: 1px solid #1a2947;
    border-radius: 10px;
    padding: 20px !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
  }
  pre code {
    background: transparent;
    color: #e2e8f0;
    font-size: 0.85em;
  }
  pre code .hljs-keyword,
  pre code .hljs-selector-tag,
  pre code .hljs-built_in,
  pre code .hljs-meta {
    color: #7dd3fc;
  }
  pre code .hljs-string,
  pre code .hljs-attr {
    color: #86efac;
  }
  pre code .hljs-number,
  pre code .hljs-literal {
    color: #fbbf24;
  }
  pre code .hljs-variable,
  pre code .hljs-template-variable,
  pre code .hljs-tag {
    color: #f9a8d4;
  }
  pre code .hljs-comment {
    color: #64748b;
  }
  pre code .hljs-title,
  pre code .hljs-section,
  pre code .hljs-type {
    color: #67e8f9;
  }
  pre code .hljs-addition {
    color: #86efac;
  }
  pre code .hljs-deletion {
    color: #fca5a5;
  }
  pre code .hljs-symbol,
  pre code .hljs-bullet,
  pre code .hljs-link {
    color: #c4b5fd;
  }
  pre code .hljs-code {
    color: #93c5fd;
  }
  pre code .hljs-strong {
    color: #fbbf24;
    font-weight: 700;
  }
  pre code .hljs-emphasis {
    color: #67e8f9;
    font-style: italic;
  }
  strong {
    color: #20e0af;
  }
  em {
    color: #009efd;
    font-style: italic;
  }
  blockquote {
    border-left: 4px solid #20e0af;
    background: #0f1d35;
    padding: 12px 20px;
    border-radius: 0 10px 10px 0;
    color: #d0dae4;
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
    color: #ffffff;
    border-bottom: 4px solid #20e0af;
  }
  section.lead p {
    color: #b8c8d8;
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
    background: #0a1424 !important;
  }
  .cols .desc {
    flex: 1;
  }
  .cols .desc h3 {
    margin-top: 0;
  }
  a {
    color: #5cc8ff;
  }
  a:hover {
    color: #7dd6ff;
  }
  section::after {
    color: #8899aa;
  }
  footer {
    color: #7a90a5;
    font-size: 0.7em;
  }
---

<!-- _class: lead -->

# The Anatomy of a Harbor Task

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

- Define role and goal clearly.
- Specify constraints (e.g., "DO NOT MODIFY main.go").
- Mention expected output location.

```md
You are expert Go programmer.
Your task is to compile Go program from source
code located in `/app/src` and produce a working binary at `/app/bin/main`.
Do not modify any Go files.
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

- `Dockerfile` — environment in which the tasks runs.
- Input files: code and data (need to be explicitly copied).
- `docker-compose.yaml` _(optional)_ for complex setups or network isolation.

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

- `test.sh` — main verification script.
- It executes tests (e.g. `pytest`, `diff`) inside the environment.
- Writes score `1` (success) or `0` (failure) to `/logs/verifier/reward.txt`.
- Support of multidimensional metrics with `reward.json`.

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

- Running `solve.sh` should make **all tests pass**.
- _Optional_, but useful for checking tests.
- Required for public benchmarks. e.g. TerminalBench.

```bash
harbor run -p "tasks/example-task" --agent oracle
```

</div></div>

---

## Running the example task

```bash
export OPENROUTER_API_KEY=...
```

```bash
harbor run -p "tasks/example-task"
  --agent terminus-2
  --model openrouter/anthropic/claude-haiku-4.5
```

An interactive preview of the results:

```bash
harbor view jobs/
```

---

## Agents

```bash
export ANTHROPIC_API_KEY=sk-ant-api03-...
harbor run -p "tasks/example-task" --agent claude-code
```

Default is `terminus-2` by Laude Institute.

Multiple agents are available: `gemini-cli`, `claude-code`, `codex`, `cursor-cli`.

---

## Environments

```bash
harbor run -p "tasks/example-task"
  --agent terminus-2
  --model openrouter/anthropic/claude-haiku-4.5
  --env daytona
```

- The default is a local Docker environment.
- Built-in support for remote environments, e.g. [Daytona](https://www.daytona.io/).
- Requires `DAYTONA_API_KEY`.

---

## Task inspiration

- [www.tbench.ai/registry/terminal-bench/2.0](https://www.tbench.ai/registry/terminal-bench/2.0) – Terminal Bench 2.0
- [quesma.com/benchmarks/](https://quesma.com/benchmarks/) – Quesma's public benchmarks: OTelBench, CompileBench, BinaryAudit (**released this week!**)

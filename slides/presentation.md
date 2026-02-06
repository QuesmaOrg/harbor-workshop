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

## The Big Picture

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
        ├── test.sh
        └── test_outputs.py
```

**2 files** + **3 folders** - that's all you need*.*

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
        ├── test.sh
        └── test_outputs.py
```

</div><div class="desc">

### Task metadata

Contains:
- **Author name**
- **Labels**
- Task-specific settings

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
        ├── test.sh
        └── test_outputs.py
```

</div><div class="desc">

### The prompt for the LLM Agent

The actual assignment — think of it as the prompt that tells the agent *what to do*.

> Consult the "How to write a quality task" section for guidance.

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
        ├── test.sh
        └── test_outputs.py
```

</div><div class="desc">

### The world your task lives in

- `Dockerfile` — builds the container where the task runs
- Source files — all required sources go here
- `docker-compose.yaml` *(optional)* — enforces *network isolation* (recommended)

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
        ├── test.sh      ◄
        └── test_outputs.py ◄
```

</div><div class="desc">

### How we know the agent succeeded

- `test.sh` — boilerplate, **copy unchanged**
  Harbor copies & executes it inside the container
- `test_outputs.py` — **your actual test logic**
  Verify the agent's work (e.g. binary exists, program runs)

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
        ├── test.sh
        └── test_outputs.py
```

</div><div class="desc">

### Reference implementation

Running `solve.sh` should make **all tests pass**.

This folder is *optional* — for compile-bench tasks, specifying a solution is not required.

</div></div>

---

<!-- _class: lead -->

# Recap

`task.toml` + `instruction.md` define **what**
`environment/` defines **where**
`tests/` define **success criteria**
`solution/` shows **one way to get there**
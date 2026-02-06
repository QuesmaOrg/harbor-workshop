# llm-day

This repository contains all the necessary materials for 
**1h Workshop: Hands-on AI agent evaluation: building benchmarks with Harbor** we ran during 
[LLMday Warsaw](https://llmday.com/2026-warsaw-q1/) on Feb 12th, 2026.


# How to use this repository

### Prerequisites

Make sure you have following tools installed:
* [Harbor](https://harborframework.com) - main tool which is going to execute LLM tasks and test the results.
    We recommend installing Harbor system-wide with [uv](https://docs.astral.sh/uv/): `uv tool install harbor`,
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) - all the tasks are executed locally within Docker containers.

### Environment setup
The workshop examples will run task in Docker containers and use [OpenRouter](https://openrouter.ai) for LLM API calls.
To run the examples you need to set the `OPENROUTER_API_KEY` environment variable.
```bash
export OPENROUTER_API_KEY=...
```

Make sure you have both Harbor and Docker installed:
```bash
harbor --version
docker ps
```

## Running example tasks

Running basic task:
```bash
harbor run -p "tasks/example-task" --agent terminus-2 --model openrouter/anthropic/claude-sonnet-4.5
```

Task run results are stored in `jobs/` directory. There is a nice UI available within Harbor:
```bash 
harbor view jobs/  
```

Using different agents:
```bash
ANTHROPIC_API_KEY=sk-ant-api03-... \
harbor run -p "tasks/example-task" --agent claude-code
```

Task with multiple runs – three trials, two concurrent runs: 
```bash
harbor run -p "tasks/example-task" --agent terminus-2 --model openrouter/anthropic/claude-sonnet-4.5 -n 2 -k 3 
```

Tasks can be organized in directories ("datasets")
```bash
harbor run  --agent terminus-2 --model openrouter/anthropic/claude-sonnet-4.5  -p tasks/ \
    -n 2 \
    -t "example*"
```

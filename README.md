# Hands-on AI agent evaluation: building benchmarks with Harbor

This repository contains all the necessary materials for
**1h Workshop: Hands-on AI agent evaluation: building benchmarks with Harbor** we ran during
[LLMday Warsaw](https://llmday.com/2026-warsaw-q1/) on 12th Feb 2026.

Slides:

- [Benchmarks everywhere](https://www.dropbox.com/scl/fi/0yva9lqaeqpvv0f2t4pvu/20260212-llmday-harbor-benchmark.pdf?rlkey=nsh08qqnq9sedkiomr018lqnw&dl=0)
- [Harbor task structure](https://quesmaorg.github.io/harbor-workshop/)

## Prerequisites

Make sure you have the following tools installed:

- [Harbor](https://harborframework.com) - main tool which is going to execute LLM tasks and test the results.
  - We recommend installing Harbor system-wide with [uv](https://docs.astral.sh/uv/): `uv tool install harbor`,
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) - all the tasks are executed locally within Docker containers.
- LLM API keys (if you don't have one, we are happy to provide!)
  - During this workshop, [OpenRouter](https://openrouter.ai) for LLM API calls so easly access models by various providers.

Set:

```bash
export OPENROUTER_API_KEY=...
```

Make sure you have both Harbor and Docker installed:

```bash
harbor --version  # 0.1.43 or above
docker --version  # 29.0.1 or above
```

Make sure varibles are set and Docker is running:

```bash
env | grep "OPENROUTER_API_KEY"
docker ps
```

## Running example tasks

Running basic task:

```bash
harbor run -p "tasks/example-task" --agent terminus-2 --model openrouter/anthropic/claude-haiku-4.5
```

Task run results are stored in `jobs/` directory. There is a nice UI available within Harbor:

```bash
harbor view jobs/
```

Using different agents, for example Claude Code:

```bash
ANTHROPIC_API_KEY=sk-ant-api03-... \
harbor run -p "tasks/example-task" --agent claude-code --model claude-sonnet-4-5-20250929
```

Take a note that different providers may have different names for the same model, here is [a list of models by Anthropic](https://platform.claude.com/docs/en/about-claude/models/overview)

Task with multiple runs – `k=3` trials, `n=2` concurrent runs:

```bash
harbor run -p "tasks/example-task" -a terminus-2 -m openrouter/anthropic/claude-haiku-4.5 -k 3 -n 2
```

Tasks can be organized in [datasets](https://harborframework.com/docs/datasets#harbor-registry):

```bash
harbor run \
  --dataset compilebench@1.0 \
  --task-name "c*" \
  --agent terminus-2 \
  --model openai/gpt-5.2
```

Harbor is generally helpful. To get summary of harbor options, see:

```bash
harbor run --help
```

## Notes

- [Terminal Bench 2.0](https://www.tbench.ai/) - including [tasks](https://www.tbench.ai/registry/terminal-bench/2.0)
- [Our benchmarks at Quesma](https://quesma.com/benchmarks/)
- [Migrating CompileBench to Harbor: standardizing AI agent evals](https://quesma.com/blog/compilebench-in-harbor/) blog post

# Python for DevOps + Agentic AI

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=elviDev&theme=github-light&cache_seconds=1800&v=3" alt="Elvis's Contribution Graph" width="100%" />
</p>

Learn to use Python for real DevOps work — automation, cloud operations,
log analysis, internal tooling, and local AI agents.

The focus is not Python syntax for its own sake, but thinking like a DevOps
engineer using Python. The course is organized into topic modules (not days),
so you can follow it live, watch it recorded, or jump straight to the topic you
need.

New here? Read [START-HERE.md](START-HERE.md), then set up your machine with
[SETUP.md](SETUP.md).

---

## Objective

By the end, you'll be able to say (and prove) "I use Python to solve DevOps
problems."

Each module is self-contained: its own README with runnable scripts, a practice
section to try yourself, and any sample data it needs.

---

## Modules

Recommended learning path (each module stands alone, but this order builds
naturally):

| Module | You'll learn |
|--------|--------------|
| [01-python-foundations](01-python-foundations/) | Variables, control flow, functions, `psutil` system health |
| [02-apis-and-json](02-apis-and-json/) | `requests`, JSON, dict/list/set, file I/O, env-var secrets |
| [03-file-handling-and-logs](03-file-handling-and-logs/) | Reading files, counting log levels, writing summaries |
| [04-object-oriented-python](04-object-oriented-python/) | Practical OOP — the log analyzer as a class |
| [05-cli-tools-argparse](05-cli-tools-argparse/) | Real CLI tools with `argparse` |
| [06-aws-automation-boto3](06-aws-automation-boto3/) | Boto3 (read-only), AWS reporting, IaC intro with CDK |
| [07-apis-with-fastapi](07-apis-with-fastapi/) | Internal DevOps APIs with FastAPI + uvicorn |
| [08-ai-agents-for-devops](08-ai-agents-for-devops/) | Local AI agents: LangGraph + LangChain + Ollama |
| [capstone](capstone/) | Assemble it all into one interview-ready project |
| [guides](guides/) | Design thinking, S.T.A.R interviews, DevOps mindset |

Each module keeps whatever structure fits it: the smaller topics are just a
README plus a script or two, while the bigger ones (`07-apis-with-fastapi`,
`08-ai-agents-for-devops`) are full project folders. Every module's README has a
Practice section with something to build yourself.

---

## Tech stack

- Python 3.10+ (3.13 recommended)
- `psutil` — system metrics
- `requests` — HTTP / APIs
- `boto3` — AWS automation; AWS CDK for IaC
- `FastAPI` + `uvicorn` — internal APIs
- `LangGraph` + `LangChain` + `Ollama` — local AI agents
- `argparse`, `json` — CLI tooling and data (standard library)

---

## Getting started

```bash
git clone <your-fork-url>
cd python-for-devops

# create a virtual environment
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# option A: install everything for the whole course
pip install -r requirements.txt

# option B: install just one module's deps
pip install -r 01-python-foundations/requirements.txt
```

Then open any module's `README.md` and follow along.

The AI agents module additionally needs [Ollama](https://ollama.com) running
locally with `llama3.2` pulled — see
[08-ai-agents-for-devops/README.md](08-ai-agents-for-devops/README.md).

---

## Projects included

- System Health Monitor — CPU / memory / disk checks (`01-python-foundations`)
- Log Analyzer — script to OOP to CLI (`03-file-handling-and-logs`, `04-object-oriented-python`, `05-cli-tools-argparse`)
- AWS Resource Report — read-only S3 / EC2 reporting (`06-aws-automation-boto3`)
- Internal DevOps Utilities API — FastAPI service exposing metrics, logs and AWS info (`07-apis-with-fastapi`)
- Local Log Analysis Agent — LangGraph + Ollama AI agent (`08-ai-agents-for-devops`)
- Capstone — one clean end-to-end flow tying it together (`capstone`)

---

## Who this is for

- Beginners in Python
- DevOps, SRE, Cloud, and Automation engineers
- Freshers and career switchers adding Python automation skills

---

## How to use this repository

1. Fork the repo; sync your fork to get updates.
2. Create and activate a virtual environment.
3. Install dependencies (whole course or per-module).
4. Work through modules in order, or jump to the topic you need.
5. Try the Practice section in each module's README.
6. Push your work and share your progress.

---

Happy Learning

**TrainWithShubham**

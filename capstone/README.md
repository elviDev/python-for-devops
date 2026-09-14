# Capstone — Python for DevOps

The capstone ties the whole course together into one project. You don't need
every piece — even one clean, working, end-to-end flow is enough to be
interview-ready.

---

## My implementation

A FastAPI service — "DevOps Intelligence API" — covering the full "Impressive"
tier: log analysis, system metrics, AWS resource visibility, and an
AI-assisted log investigation endpoint backed by a local Ollama model.

### Endpoints

| Method | Path           | What it does                                      |
| ------ | -------------- | -------------------------------------------------- |
| GET    | `/health`      | Liveness check                                      |
| GET    | `/logs`        | INFO/WARNING/ERROR counts for a log file            |
| GET    | `/metrics`     | Current CPU, memory, and disk usage                 |
| GET    | `/aws/s3`      | S3 buckets grouped by age                           |
| GET    | `/aws/ec2`     | EC2 instances and their state                       |
| GET    | `/aws/report`  | Combined S3 + EC2 inventory                         |
| POST   | `/ai/analyze`  | Plain-English log summary from a local LLM agent    |

### Setup

```bash
cd capstone
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

### Run

```bash
uvicorn app.main:app --reload
```

The API is then available at `http://127.0.0.1:8000` (interactive docs at
`/docs`). `/logs` and `/ai/analyze` default to `sample_logs/app.log` if no
`file` is given.

The `/aws/*` endpoints need AWS credentials available to `boto3` (e.g. via
`aws configure` or environment variables). `/ai/analyze` needs a local
[Ollama](https://ollama.com) instance running with the model set in
`OLLAMA_MODEL` (defaults to `qwen3.6:latest`) pulled and available.

### Tests

```bash
pytest
```

All 16 tests run without live AWS credentials or a running Ollama instance —
AWS and AI calls are mocked.

---

## The story these modules tell

Every module in this course builds one capability. The capstone assembles them:

```
   log analysis          ->  03-file-handling-and-logs  +  04-object-oriented-python
        |
   run it as a CLI        ->  05-cli-tools-argparse
        |
   pull in cloud data     ->  06-aws-automation-boto3
        |
   expose it as an API    ->  07-apis-with-fastapi
        |
   add an AI layer         ->  08-ai-agents-for-devops   (optional, impressive)
```

## What to build

Pick a scope and make it clean, commented, and runnable:

- Minimum: the log analyzer as a CLI tool (`05-cli-tools-argparse`) that writes a
  JSON summary.
- Solid: wrap the log analyzer + system metrics in a FastAPI service
  (`07-apis-with-fastapi`) with `/health`, `/logs`, `/metrics`.
- Impressive: add the AWS report endpoint and/or the local AI log agent.

The reference implementation of the "Solid + AWS" tier already lives in
[`../07-apis-with-fastapi/devops-utilities-api`](../07-apis-with-fastapi/devops-utilities-api).
Use it as your starting point, or build your own.

## Deliverables

1. A working project (one clean flow is enough).
2. A project-level `README.md` explaining what it does and how to run it.
3. A **STAR explanation** (see below) you can use in interviews.

## Explain it with the S.T.A.R method

Fill in [`STAR.md`](STAR.md):

- Situation — what was the problem? (e.g. "logs grew daily; manual checks were slow")
- Task — what were you responsible for? (e.g. "automate log analysis in Python")
- Action — what did you actually do? (parse logs, CLI, API, AI summary)
- Result — what was the outcome? (faster visibility, less manual effort)

## Checklist before you call it done

- [ ] Code runs without errors from a clean `venv`
- [ ] `README.md` explains setup + run steps
- [ ] Functions are named clearly and commented where needed
- [ ] Errors are handled (missing file, bad input, failed API call)
- [ ] `STAR.md` written and rehearsed

## What comes next

CI/CD, Kubernetes, monitoring, cloud architecture — Python for DevOps was your
foundation. Keep going: [DevOps – Zero To Hero](https://bit.ly/devops-josh).

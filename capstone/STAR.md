# My Capstone — S.T.A.R Explanation

## Situation
- Our team's application logs and infrastructure health were only checked
  manually — someone had to SSH in, tail log files, and separately check AWS
  and system metrics whenever something seemed off. That was slow, easy to
  forget, and gave no consistent way to check status on demand.

## Task
- I was responsible for automating this with Python: parse and summarize
  application logs, expose system health metrics, surface AWS resource
  inventory, and make all of it available through a single, reusable service
  instead of one-off scripts.

## Action
- Wrote a log parser that reads a log file and counts INFO/WARNING/ERROR
  occurrences using whole-word matching, then wrapped it in an
  `analyze_log_file` function returning structured counts.
- Built a `psutil`-based metrics service reporting CPU, memory, and disk
  usage, with a configurable CPU threshold that flags the system as healthy
  or under high load.
- Used `boto3` to build an AWS inventory service: S3 buckets grouped by age
  (new vs. old, based on a configurable day threshold) and EC2 instances with
  their current state.
- Exposed all of it through a FastAPI service (`/health`, `/logs`, `/metrics`,
  `/aws/s3`, `/aws/ec2`, `/aws/report`) with routers, services, and Pydantic
  schemas kept in separate layers, and consistent HTTP error mapping
  (404/400/500/502) for missing files, bad input, and AWS/API failures.
- Added a local AI layer: a LangChain/LangGraph agent running against a local
  Ollama model, given a tool that returns the exact deterministic log counts
  so it can't invent statistics, exposed via `POST /ai/analyze`. Added
  path-traversal protection so the endpoint can only read `.log` files inside
  the approved log directory.
- Wrote 16 unit tests covering the log parser, metrics service, AWS service
  (mocking `boto3` clients so no real AWS calls are made in tests), and the
  AI router's path-resolution and security checks.

## Result
- Replaced manual log/metrics/AWS checks with a single running API that
  answers each question in one request instead of several manual steps.
- The AI endpoint gives a plain-English read of what a log file shows,
  grounded in the same deterministic counts the API reports elsewhere, which
  makes it trustworthy enough to actually rely on rather than just a demo.
- All 16 tests pass and the AWS/AI tests run without needing live AWS
  credentials or a running Ollama instance, so the suite is safe to run in
  CI.

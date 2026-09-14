from collections import Counter
from pathlib import Path


LEVELS = ("INFO", "WARNING", "ERROR")


def read_log_file(path: str | Path) -> str:
    """Read a UTF-8 log file and return its contents."""
    log_path = Path(path)

    if not log_path.exists():
        raise FileNotFoundError(f"Log file not found: {log_path}")

    if not log_path.is_file():
        raise ValueError(f"Log path is not a file: {log_path}")

    return log_path.read_text(encoding="utf-8")


def count_log_levels(text: str) -> dict[str, int]:
    """Count INFO, WARNING and ERROR occurrences by whole-word matching."""
    counts = Counter()

    for line in text.splitlines():
        tokens = set(line.split())

        for level in LEVELS:
            if level in tokens:
                counts[level] += 1

    return {level: counts.get(level, 0) for level in LEVELS}


def analyze_log_file(path: str | Path) -> dict:
    """Read and analyze a log file."""
    text = read_log_file(path)
    counts = count_log_levels(text)

    return {
        "log_file": str(path),
        "counts": counts,
        "total_lines": len(text.splitlines()),
    }
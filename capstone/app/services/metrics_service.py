import psutil


DEFAULT_CPU_THRESHOLD = 85.0


def get_system_metrics(
    cpu_threshold: float = DEFAULT_CPU_THRESHOLD,
) -> dict:
    """
    Return current CPU, memory, and disk usage.

    The CPU threshold determines whether the system is reported as healthy
    or experiencing high CPU usage.
    """
    if not 0 <= cpu_threshold <= 100:
        raise ValueError("cpu_threshold must be between 0 and 100")

    cpu_percent = psutil.cpu_percent(interval=0.5)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent

    status = (
        "High CPU"
        if cpu_percent > cpu_threshold
        else "Healthy"
    )

    return {
        "cpu_percentage": cpu_percent,
        "memory_percentage": memory_percent,
        "disk_percentage": disk_percent,
        "cpu_threshold": cpu_threshold,
        "system_status": status,
    }
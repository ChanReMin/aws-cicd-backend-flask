# Bind to all interfaces; PORT en   v var can override in runtime command if needed
bind = "0.0.0.0:8000"

# A sensible default: 2-4 workers per CPU core (here: 2 * cores)
import multiprocessing
workers = max(2, multiprocessing.cpu_count() * 2)

# Threaded workers are fine for typical Flask I/O workloads
threads = 2

# Graceful timeouts
timeout = 30
graceful_timeout = 30

# Access & error logs to stdout/stderr (Docker best practice)
accesslog = "-"
errorlog = "-"
loglevel = "info"

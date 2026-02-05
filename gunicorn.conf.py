import multiprocessing
import os

# Recommended formula: workers = 2 * cpu + 1
workers = int(os.environ.get('GUNICORN_WORKERS') or (2 * multiprocessing.cpu_count() + 1))
bind = f"0.0.0.0:{os.environ.get('PORT', '5000')}"
# You can tune timeout for your environment
timeout = int(os.environ.get('GUNICORN_TIMEOUT', 30))

# Logging
accesslog = '-'  # stdout
errorlog = '-'   # stderr
loglevel = os.environ.get('GUNICORN_LOGLEVEL', 'info')

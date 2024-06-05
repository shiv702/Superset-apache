from datetime import timedelta
from worker_app import app  # Importing the Celery app from worker_app.py

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'worker_app.add',  # Reference the task defined in worker_app.py
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}


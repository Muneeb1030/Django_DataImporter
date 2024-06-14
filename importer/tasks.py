from redisandcelery.celery import app
from celery import shared_task
import time

@app.task
def celery_test_task():
    time.sleep(10)
    return "Done"
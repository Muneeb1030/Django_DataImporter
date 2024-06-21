from redisandcelery.celery import app
import time
from django.core.management import call_command

@app.task
def celery_test_task():
    time.sleep(10)
    return "Done"

@app.task
def Import_data(file_path, model_name):
    call_command('importdata', file_path,model_name)
    return "Done Inserting"
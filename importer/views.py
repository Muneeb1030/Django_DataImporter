from django.shortcuts import render
from django.http import HttpResponse
from importer.tasks import celery_test_task
from django.http import HttpResponse
from .models import get_db
def importdata(request):
    db = get_db()
    collections = db.list_collection_names()
    if request.method == 'POST':
       
        return render(request, 'importer/importdata.html', {'collections': collections})
    else:
        return render(request, 'importer/importdata.html',{'collections': collections})

def celery_task(request):
    celery_test_task.delay()
    return HttpResponse("Done")

def trigger_error(request):
    return HttpResponse(1 / 1)
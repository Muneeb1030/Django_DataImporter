from django.shortcuts import render, redirect
from django.http import HttpResponse
from importer.tasks import celery_test_task, Import_data
from django.http import HttpResponse
from .models import get_db
from upload.models import Upload
from django.conf import settings
def importdata(request):
    db = get_db()
    collections = db.list_collection_names()
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get("model_name")
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        file_rel = str(upload.file.url)
        file_abs = str(settings.BASE_DIR)
        file_path = file_abs + file_rel
        Import_data.delay(file_path, model_name)
        return redirect('importdata')
    else:
        return render(request, 'importer/importdata.html',{'collections': collections})

def celery_task(request):
    celery_test_task.delay()
    return HttpResponse("Done")

def trigger_error(request):
    return HttpResponse(1 / 1)
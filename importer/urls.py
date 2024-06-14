from django.urls import path
from . import views
urlpatterns = [
    path("", views.importdata, name="importdata"),
    path("celery", views.celery_task, name="celery_test_task"),
    path("error", views.trigger_error, name="trigger_error"),
]

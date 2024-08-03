from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("importer/", include("importer.urls")),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

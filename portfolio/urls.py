from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("resume/", views.resume, name="resume"),
    path("videos/", views.videos, name="videos"),
    path("projects/", views.projects, name="projects"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

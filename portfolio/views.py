from django.shortcuts import render
from .models import PersonalInfo, Home, Video, Project, Resume
from .forms import HomeForm, VideoForm
from django.views.generic import ListView


def home(request):
    personal_info = PersonalInfo.objects.first()
    home_content = Home.objects.all()
    return render(
        request,
        "home.html",
        {"personal_info": personal_info, "home_content": home_content},
    )


def resume(request):
    personal_info = PersonalInfo.objects.first()
    resume = Resume.objects.first()
    return render(
        request, "resume.html", {"personal_info": personal_info, "resume": resume}
    )


def videos(request):
    personal_info = PersonalInfo.objects.first()
    video_content = Video.objects.all()
    return render(
        request,
        "others.html",
        {"personal_info": personal_info, "video_content": video_content},
    )


def projects(request):
    personal_info = PersonalInfo.objects.first()
    project_content = Project.objects.all()
    return render(
        request,
        "projects.html",
        {"personal_info": personal_info, "project_content": project_content},
    )


class ProjectListView(ListView):
    model = Project
    template_name = "projects.html"
    context_object_name = "project_content"


def edit_home(request):
    if request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HomeForm()
    return render(request, "edit_home.html", {"form": form})


def edit_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VideoForm()
    return render(request, "edit_video.html", {"form": form})

from django.db import models
from tinymce.models import HTMLField
from django.db.models.signals import pre_save
from django.dispatch import receiver


class PersonalInfo(models.Model):
    image = models.ImageField(upload_to="personal_info/")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    substack_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=PersonalInfo)
def limit_personal_info(sender, instance, **kwargs):
    if PersonalInfo.objects.exists() and not instance.pk:
        raise Exception("Only one PersonalInfo object is allowed.")


class Resume(models.Model):
    document = models.FileField(upload_to="resumes/")

    def __str__(self):
        return "Resume"


class Home(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    paragraph = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title


def resume(request):
    personal_info = PersonalInfo.objects.first()
    resume = Resume.objects.first()
    return render(
        request, "resume.html", {"personal_info": personal_info, "resume": resume}
    )


class Video(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    paragraph = HTMLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    image = models.ImageField(upload_to="projects/")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

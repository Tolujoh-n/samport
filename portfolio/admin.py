from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from .models import PersonalInfo, Home, Video, Project, Tag, Resume


class RichTextAdminForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = "__all__"

    paragraph = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 10}))


class HomeAdmin(admin.ModelAdmin):
    form = RichTextAdminForm


class VideoAdmin(admin.ModelAdmin):
    form = RichTextAdminForm


class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "document",
    )


admin.site.register(PersonalInfo)
admin.site.register(Home, HomeAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Resume)
admin.site.register(Project)
admin.site.register(Tag)

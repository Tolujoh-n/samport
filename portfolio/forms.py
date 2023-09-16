from django import forms
from tinymce.widgets import TinyMCE
from .models import Home, Video


class RichTextForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = "__all__"

    paragraph = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 10}))


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ["title", "paragraph"]


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["title", "paragraph", "video_link"]

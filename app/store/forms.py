from django import forms
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms import ModelForm

from applipsync.models import File, Mouth, Question


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class FileUploadForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mouth"].queryset = Mouth.objects.filter(
            Q(user=user) | Q(user__username="admin")
        )

    class Meta:
        model = File
        # fields = ('__all__')
        fields = ("audio", "script", "name", "host", "mouth", "user")
        widgets = {"host": forms.HiddenInput(), "user": forms.HiddenInput()}


class FileUploadFormCreate(ModelForm):
    class Meta:
        model = File
        # fields = ('__all__')
        fields = ("audio", "script", "name", "host", "mouth", "user")
        widgets = {"host": forms.HiddenInput(), "user": forms.HiddenInput()}


class MouthForm(ModelForm):
    class Meta:
        model = Mouth
        fields = "__all__"
        widgets = {"host": forms.HiddenInput(), "user": forms.HiddenInput()}
        # fields = ('audio', 'script', 'name', 'host', 'mouth')
        # widgets = {'host': forms.HiddenInput()}

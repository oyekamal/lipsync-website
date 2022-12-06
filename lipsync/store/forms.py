from django.forms import ModelForm

from django.contrib.auth.models import User
from applipsync.models import File, Mouth
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class FileUploadForm(ModelForm):
    class Meta:
        model = File
        # fields = ('__all__')
        fields = ('audio', 'script', 'name', 'host', 'mouth')
        widgets = {'host': forms.HiddenInput()}

class MouthForm(ModelForm):
    class Meta:
        model = Mouth
        fields = ('__all__')
        # fields = ('audio', 'script', 'name', 'host', 'mouth')
        # widgets = {'host': forms.HiddenInput()}


from django.forms import ModelForm

from django.contrib.auth.models import User
from applipsync.models import File

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = ('__all__')


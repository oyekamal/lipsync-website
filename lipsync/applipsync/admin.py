from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(File)
admin.site.register(GentleJson)
admin.site.register(VideoFrame)
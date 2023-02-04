from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(File)
admin.site.register(GentleJson)
admin.site.register(VideoFrame)
admin.site.register(Video)
admin.site.register(Mouth)
admin.site.register(Question)
admin.site.register(Tag)
# admin.site.register(Blog)
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}
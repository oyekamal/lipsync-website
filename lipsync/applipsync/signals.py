from .models import File, Mouth
from django.db.models.signals import post_save
from django.dispatch import receiver
from .gentle_request import gentle_json
from django_q.tasks import async_task
from .q_services import hook_funcs
from django.conf import settings
from .serializers import *
import os, shutil
basepath = settings.BASE_DIR
basepath = str(basepath).replace("\\", '/')

@receiver(post_save, sender=File)
def qjob(sender, instance, created, **kwargs):
    if created:
        serializer = FileSerializer(instance)

        data = {
            'audio': serializer.data.get('audio'),
            'script': serializer.data.get('script'),
            'base': basepath,
            'file_id':serializer.data.get('id'),
            "baseUrl":serializer.data.get('host'),
            "mouth":serializer.data.get('mouth')
        }

        print("------------------------signal----------------------------")
        print(instance)

        print('--------------------------------')
        print(data)
        print("------------------------signal end----------------------------")
        # gentle_json(data)
        async_task(gentle_json,data, hook=hook_funcs)
        
@receiver(post_save, sender=Mouth)
def updatePath(sender, instance, created, **kwargs):
        # >>> initial_path = car.photo.path
        # >>> car.photo.name = 'cars/chevy_ii.jpg'
        # >>> new_path = settings.MEDIA_ROOT + car.photo.name
        # >>> # Move the file on the filesystem
        # >>> os.rename(initial_path, new_path)
        # >>> car.save()
        # >>> car.photo.path
        # '/media/cars/chevy_ii.jpg'
        # >>> car.photo.path == new_path
    if created:
        print("creating folder")
        folder_name = instance.title
        print("creating folder "+ folder_name)
        media_path = settings.MEDIA_ROOT 
        path = media_path + "/images/" + folder_name
        print('path  ',path)
        if not os.path.exists(path):
            print("creating folder ")
            os.makedirs(path)
        else:
            print("path found")

        folder_name = instance.title
        shutil.move(instance.a_e_h.path, path+'/a_e_h.png')
        instance.a_e_h.path = str(path) +'/a_e_h.png'
        instance.save()
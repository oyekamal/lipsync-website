import os
import shutil
import uuid

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task

from .gentle_request import gentle_json
from .models import File, Mouth
from .q_services import hook_funcs
from .serializers import *

uuid.uuid4().hex[:6].upper()
basepath = settings.BASE_DIR
basepath = str(basepath).replace("\\", "/")


@receiver(post_save, sender=File)
def qjob(sender, instance, created, **kwargs):
    if created:
        instance.slug = (
            instance.name.replace(" ", "_") + "_" + uuid.uuid4().hex[:6].upper()
        )
        instance.save()
        serializer = FileSerializer(instance)

        data = {
            "audio": serializer.data.get("audio"),
            "script": serializer.data.get("script"),
            "base": basepath,
            "file_id": serializer.data.get("id"),
            "baseUrl": serializer.data.get("host"),
            "mouth": serializer.data.get("mouth"),
        }

        print("------------------------signal----------------------------")
        print(instance)

        print("--------------------------------")
        print(data)
        print("------------------------signal end----------------------------")
        # gentle_json(data)
        async_task(gentle_json, data, hook=hook_funcs)


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
        # print("creating folder")
        folder_name = instance.title
        # print("creating folder " + folder_name)
        media_path = settings.MEDIA_ROOT
        path = media_path + "/images/" + folder_name
        print("path  ", path)
        if not os.path.exists(path):
            print("creating folder ")
            os.makedirs(path)
        else:
            print("path found")

        folder_name = instance.title

        # a_e_h
        shutil.move(instance.a_e_h.path, path + "/a_e_h.png")
        instance.a_e_h.name = f"images/{folder_name}/a_e_h.png"

        # d_j_ch_h
        shutil.move(instance.d_j_ch_h.path, path + "/d_j_ch_h.png")
        instance.d_j_ch_h.name = f"images/{folder_name}/d_j_ch_h.png"

        # f_h
        shutil.move(instance.f_h.path, path + "/f_h.png")
        instance.f_h.name = f"images/{folder_name}/f_h.png"

        # l_h
        shutil.move(instance.l_h.path, path + "/l_h.png")
        instance.l_h.name = f"images/{folder_name}/l_h.png"

        # m_b_close_h
        shutil.move(instance.m_b_close_h.path, path + "/m_b_close_h.png")
        instance.m_b_close_h.name = f"images/{folder_name}/m_b_close_h.png"

        # o_big_h
        shutil.move(instance.o_big_h.path, path + "/o_big_h.png")
        instance.o_big_h.name = f"images/{folder_name}/o_big_h.png"

        # o_small_h
        shutil.move(instance.o_small_h.path, path + "/o_small_h.png")
        instance.o_small_h.name = f"images/{folder_name}/o_small_h.png"

        # oh_h
        shutil.move(instance.oh_h.path, path + "/oh_h.png")
        instance.oh_h.name = f"images/{folder_name}/oh_h.png"

        # th_h
        shutil.move(instance.th_h.path, path + "/th_h.png")
        instance.th_h.name = f"images/{folder_name}/th_h.png"

        # trans_h
        shutil.move(instance.trans_h.path, path + "/trans_h.png")
        instance.trans_h.name = f"images/{folder_name}/trans_h.png"

        instance.save()
        # instance.a_e_h.path = str(path) +'/a_e_h.png'
        # instance.save()

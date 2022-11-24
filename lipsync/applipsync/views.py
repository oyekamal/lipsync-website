from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from.models import *
from.serializers import *
from .gentle_request import gentle_json
from django_q.tasks import async_task
from .q_services import sleepy_func, hook_funcs
from django.conf import settings
basepath = settings.BASE_DIR


# async_task('time.sleep', 22)
class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


    def create(self, request, *args, **kwargs):
        print("yes working")
        serializer = self.get_serializer(data=request.data)
        print(request.data.get('audio'))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print("serializer.data ",serializer.data)
        audio =serializer.data.get('audio')
        script =serializer.data.get('script')
        # json = gentle_json(request.data.get('audio'), request.data.get('script'))
        async_task(gentle_json, audio, script,basepath, hook=hook_funcs)

        # print(json)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
from django.conf import settings
from django.urls import reverse
from django_q.tasks import async_task
from rest_framework import status, viewsets
from rest_framework.response import Response

from .frametoVideo import convert_frames_to_video_function
from .gentle_request import gentle_json
from .models import *
from .q_services import hook_funcs, hook_video, sleepy_func
from .serializers import *
from .utils import frame_creater, framer_reader

basepath = settings.BASE_DIR
basepath = str(basepath).replace("\\", "/")


# async_task('time.sleep', 22)
class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        print("yes working")
        request.data._mutable = True
        request.data["host"] = f"{request.scheme}://{request.META['HTTP_HOST']}"
        request.data._mutable = False

        serializer = self.get_serializer(data=request.data)
        print(request.data.get("audio"))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print("serializer.data ", serializer.data)
        audio = serializer.data.get("audio")
        script = serializer.data.get("script")
        data = {
            "audio": audio,
            "script": script,
            "base": basepath,
            "file_id": serializer.data.get("id"),
            "baseUrl": f"{request.scheme}://{request.META['HTTP_HOST']}",
        }
        # json = gentle_json(request.data.get('audio'), request.data.get('script'))
        async_task(gentle_json, data, hook=hook_funcs)

        # print(json)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class VideoFrameViewSet(viewsets.ModelViewSet):
    queryset = VideoFrame.objects.all()
    serializer_class = VideoFrameSerializer

    def create(self, request, *args, **kwargs):
        print("video frmae")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        print("serializer.data ", request.data)
        # print("basepath --" ,basepath)
        print("gentle_json ", request.data.get("gentle_josn"))
        try:
            #     print(" static_url  ",settings.STATIC_URL)
            #     print(" media_url  ",settings.MEDIA_URL)
            #     print('base URL', f"{ request.scheme } :// { request.META['HTTP_HOST'] } { request.path }")
            gentle_json = GentleJson.objects.get(id=request.data.get("gentle_josn"))
            frame_list = framer_reader(gentle_json.json)
            # print("frame_list: ", frame_list)
            # request.data['video_frame'] = frame_list
            video_frame_keys = frame_creater(frame_list)
            # print(video_frame_keys)
            videoframe = VideoFrame.objects.create(
                gentle_josn=gentle_json,
                video_frame=frame_list,
                video_frame_keys=video_frame_keys,
            )
            data = {
                "pathIn": basepath + "/media/frames/",
                "pathOut": basepath + "/media/video/{}.avi".format("audio_name"),
                "video_output": "/media/video/{}.avi".format("audio_name"),
                "fps": 24.0,
                "frame_data": video_frame_keys,
                "baseUrl": f"{request.scheme}://{request.META['HTTP_HOST']}",
                "videoframe": videoframe,
            }
            # convert_frames_to_video_function(data)

            async_task(convert_frames_to_video_function, data, hook=hook_video)
        except Exception as e:
            print("found error")
            print(e)
        # # audio =serializer.data.get('audio')
        # script =serializer.data.get('script')
        # data = {
        #     'audio': audio,
        #     'script': script,
        #     'base': basepath,
        #     'file_id':serializer.data.get('id')
        # }
        # # json = gentle_json(request.data.get('audio'), request.data.get('script'))
        # async_task(gentle_json,data, hook=hook_funcs)

        # print(json)

        # self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

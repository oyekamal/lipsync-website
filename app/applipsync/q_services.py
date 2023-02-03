import time

from django_q.tasks import async_task

from .frametoVideo import convert_frames_to_video_function
from .models import File, GentleJson, Video, VideoFrame
from .utils import add_normal_phonemes, frame_creater, framer_reader


def hook_funcs(task):
    print("yes save the json")
    print("type --------------------", type(task.result.get("gentle_data")))
    file = File.objects.get(id=task.result.get("file_id"))
    json = add_normal_phonemes(task.result.get("gentle_data"))
    basepath = task.result.get("base")
    gentle_json = GentleJson.objects.create(file=file, json=json)
    frame_list = framer_reader(gentle_json.json, file.mouth.title)
    video_frame_keys = frame_creater(frame_list)
    # print(video_frame_keys)
    videoframe = VideoFrame.objects.create(
        gentle_josn=gentle_json,
        video_frame=frame_list,
        video_frame_keys=video_frame_keys,
    )
    data = {
        "pathIn": basepath + "/media/frames/",
        "pathOut": basepath + "/media/video/{}.avi".format(file.name),
        "video_output": "/media/video/{}.avi".format(file.name),
        "fps": 24.0,
        "frame_data": video_frame_keys,
        "baseUrl": task.result.get("baseUrl"),
        "videoframe": videoframe,
    }

    async_task(convert_frames_to_video_function, data, hook=hook_video)
    print("The result is done for : ", task.result.get("file_id"))


def hook_video(task):
    try:
        print("basaURL", task.result.get("baseUrl"))
        path = task.result.get("baseUrl") + task.result.get("video_output")
        video = Video.objects.create(
            video_frame=task.result.get("videoframe"), video=path
        )
    except Exception as e:
        print("found exception in hook_video")
        print(e)
    print("video is done ")
    # print(task.result)


def sleepy_func(junk, sleep):
    print("sleep: ", sleep * junk)
    for i in range(10):
        print("hello ", i)
        time.sleep(1)
    print("sleepy function ran")

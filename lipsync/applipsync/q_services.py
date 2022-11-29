import time
from .models import GentleJson, File, VideoFrame
from .utils import add_normal_phonemes, framer_reader
from django_q.tasks import async_task


def hook_funcs(task):
    print("yes save the json")
    print("type --------------------", type(task.result.get('gentle_data')))
    file = File.objects.get(id=task.result.get('file_id'))
    json = add_normal_phonemes(task.result.get('gentle_data'))

    gentle_json = GentleJson.objects.create(file=file, json=json)
    frame_list = framer_reader(gentle_json.json)
    VideoFrame.objects.create(gentle_josn=gentle_json, video_frame=frame_list)

    print("The result is done for : ", task.result.get('file_id'))


def sleepy_func(junk,sleep):
    print("sleep: ",sleep* junk )
    for i in range(10):
        print("hello ", i)
        time.sleep(1)
    print ("sleepy function ran")

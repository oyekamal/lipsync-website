import time
from .models import GentleJson, File, VideoFrame
from .utils import add_normal_phonemes, framer_reader, frame_creater
from django_q.tasks import async_task
from .frametoVideo import  convert_frames_to_video_function


def hook_funcs(task):
    print("yes save the json")
    print("type --------------------", type(task.result.get('gentle_data')))
    file = File.objects.get(id=task.result.get('file_id'))
    json = add_normal_phonemes(task.result.get('gentle_data'))
    basepath = task.result.get('base')
    gentle_json = GentleJson.objects.create(file=file, json=json)
    frame_list = framer_reader(gentle_json.json)
    video_frame_keys = frame_creater(frame_list)
    # print(video_frame_keys)
    VideoFrame.objects.create(gentle_josn=gentle_json, video_frame=frame_list, video_frame_keys=video_frame_keys)
    data = {
            "pathIn":basepath+'/media/frames/', 
            "pathOut":basepath+'/media/video/{}.avi'.format(file.remark), 
            "fps":24.0, 
            "frame_data":video_frame_keys
        }

    async_task(convert_frames_to_video_function,data, hook=hook_video)    
    print("The result is done for : ", task.result.get('file_id'))

def hook_video(task):
    print("video is done ")

def sleepy_func(junk,sleep):
    print("sleep: ",sleep* junk )
    for i in range(10):
        print("hello ", i)
        time.sleep(1)
    print ("sleepy function ran")

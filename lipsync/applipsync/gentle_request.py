import requests
import json
from django.conf import settings
path = settings.BASE_DIR

# from utils import add_gentle_phonemes, framer_reader, frame_creater, add_normal_phonemes
# from frametoVideo import  convert_frames_to_video_function
url = "http://localhost:49153/transcriptions?async=false"


def gentle_json(audio_file, script_file):
    url = "http://localhost:49153/transcriptions?async=false"

    path = settings.BASE_DIR

    print(script_file, '  ',audio_file)
    print("sending... requests")
    # print("BASE_DIR ",str(path))
    audio_path =  str(path).replace("\\",'/') + '/media/audio/'+audio_file.split('/')[-1]
    transcript_path =str(path).replace("\\",'/')  +  '/media/script/'+script_file.split('/')[-1]

    print(audio_path)
    print(transcript_path)

    # audio_path = audio_file
    # transcript_path = script_file


    audio_name = audio_path.split('/')[-1]
    transcript_name = transcript_path.split('/')[-1]
    file_type = 'audio/{}'.format(audio_name.split('.')[-1])
    payload = {}
    files = [
        ('audio', (audio_name, open(audio_path, 'rb'), file_type)),
        ('transcript', (transcript_name, open(transcript_path, 'rb'), 'text/plain'))
    ]
    # files = [
    #     ('audio', open(audio_file,'rb')),
    #     ('transcript',open(script_file, 'rb'))
    # ]
    headers = {}


    print("time extraction from gentle...!")
    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    gentle_data = response.text

    path = "C:/Users/cacf/Documents/website_work/lipsync/media/json"
    with open(path + "/sample_text.json", "w") as outfile:
        outfile.write(gentle_data)
    return gentle_data

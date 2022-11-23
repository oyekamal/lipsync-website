import requests
import json

# from utils import add_gentle_phonemes, framer_reader, frame_creater, add_normal_phonemes
# from frametoVideo import  convert_frames_to_video_function
url = "http://localhost:49153/transcriptions?async=false"


def gentle_json(audio_file, script_file):
    # audio_path = './files/software4.wav'
    # transcript_path = './files/software4.txt'

    # audio_path = audio_file
    # transcript_path = script_file


    # audio_name = audio_path.split('/')[-1]
    # transcript_name = transcript_path.split('/')[-1]
    # file_type = 'audio/{}'.format(audio_name.split('.')[-1])
    payload = {}
    # files = [
    #     ('audio', (audio_name, open(audio_path, 'rb'), file_type)),
    #     ('transcript', (transcript_name, open(transcript_path, 'rb'), 'text/plain'))
    # ]
    files = [
        ('audio', audio_file),
        ('transcript', script_file)
    ]
    headers = {}


    print("time extraction from gentle...!")
    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    gentle_data = response.text

    path = "C:/Users/cacf/Documents/website_work/lipsync/media/json"
    with open(path + "/sample.json", "w") as outfile:
        outfile.write(gentle_data)
    return gentle_data

import json
import time

import requests

# from django.conf import settings
# basepath = settings.BASE_DIR

# from utils import add_gentle_phonemes, framer_reader, frame_creater, add_normal_phonemes
# from frametoVideo import  convert_frames_to_video_function
url = "http://gentle:8765/transcriptions?async=false"


def gentle_json(data):
    # data = {
    #         'audio': audio,
    #         'script': script,
    #         'base': basepath,
    #         'file_id':serializer.data.get('id')
    #     }
    url = "http://gentle:8765/transcriptions?async=false"
    # url = "http://localhost:49153/transcriptions?async=false"
    # basepath = settings.BASE_DIR
    basepath = data.get("base")
    script_file = data.get("script")
    audio_file = data.get("audio")
    print("basepath  ", basepath)
    print(script_file, "  ", audio_file)
    print("sending... requests")
    # print("BASE_DIR ",str(path))
    path = str(basepath).replace("\\", "/")
    audio_path = path + "/media/audio/" + audio_file.split("/")[-1]
    transcript_path = path + "/media/script/" + script_file.split("/")[-1]

    print(audio_path)
    print(transcript_path)

    # audio_path = audio_file
    # transcript_path = script_file

    audio_name = audio_path.split("/")[-1]
    transcript_name = transcript_path.split("/")[-1]
    file_type = "audio/{}".format(audio_name.split(".")[-1])
    payload = {}
    files = [
        ("audio", (audio_name, open(audio_path, "rb"), file_type)),
        ("transcript", (transcript_name, open(transcript_path, "rb"), "text/plain")),
    ]
    # files = [
    #     ('audio', open(audio_file,'rb')),
    #     ('transcript',open(script_file, 'rb'))
    # ]
    headers = {}

    print("time extraction from gentle...!")

    gentle_data = None
    while gentle_data == None:
        try:
            response = requests.request(
                "POST", url, headers=headers, data=payload, files=files
            )
            gentle_data = response.text
            break
        except Exception as e :
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            print("exceptions : ",e)
            continue

    # json_saving_path = path + "/media/json/"
    # with open(json_saving_path + "{}.json".format(audio_name), "w") as outfile:
    #     outfile.write(gentle_data)

    data["gentle_data"] = json.loads(gentle_data)
    data["base"] = basepath
    return data

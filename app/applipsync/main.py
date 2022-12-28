import json

import requests

# from utils import add_gentle_phonemes, framer_reader, frame_creater, add_normal_phonemes
# from frametoVideo import  convert_frames_to_video_function
url = "http://gentle:8765/transcriptions?async=false"

audio_path = "./software4.wav"
transcript_path = "./software4.txt"

# audio_path = audio_path.replace('\\', '/')
# transcript_path = transcript_path.replace('\\', '/')

audio_name = audio_path.split("/")[-1]
transcript_name = transcript_path.split("/")[-1]
file_type = "audio/{}".format(audio_name.split(".")[-1])
payload = {}
files = [
    ("audio", (audio_name, open(audio_path, "rb"), file_type)),
    ("transcript", (transcript_name, open(transcript_path, "rb"), "text/plain")),
]
headers = {}


print("time extraction from gentle...!")
response = requests.request("POST", url, headers=headers, data=payload, files=files)

gentle_data = response.text

path = "."
with open(path + "/sample.json", "w") as outfile:
    outfile.write(gentle_data)
# # parse x:
# print()
# gentle_data_json = json.loads(gentle_data)

# print('adding phonemes')
# # gentle = add_gentle_phonemes(gentle_data_json)
# normal = add_normal_phonemes(gentle_data_json)

# # with open(f'./json/test_normal.json', "w") as outfile:
# #     json.dump(normal, outfile)

# # f = open('./json/test_normal.json')

# # data = json.load(f)

# print("frame editor")
# image_list = framer_reader(normal)


# print("frame creatioon")
# frame_data = frame_creater(image_list)
# print(frame_data)
# print('making video')
# convert_frames_to_video_function('./frames/', f'./video/{audio_name}.avi', 24.0, frame_data)

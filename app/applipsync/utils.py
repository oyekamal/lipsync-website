import json
import math
import os

from g2p_en import G2p
from PIL import Image

from common.constants import NORMAL_PHONEMES

from .imageutils import adding_image

g2p = G2p()
from django.conf import settings

basepath = settings.BASE_DIR


def returnSum(dict):
    return sum(dict.values())


def equalizer(diff, phonemes_frame):
    """inner sum number vales should be equal to diff"""
    sum = returnSum(phonemes_frame)
    while diff != sum:
        sum = returnSum(phonemes_frame)
        if diff == sum:
            return phonemes_frame
        elif diff <= sum:
            max_value = max(phonemes_frame, key=phonemes_frame.get)
            phonemes_frame[max_value] = phonemes_frame[max_value] - 1
        else:
            max_value = min(phonemes_frame, key=phonemes_frame.get)
            phonemes_frame[max_value] = phonemes_frame[max_value] + 1
    return phonemes_frame


def add_normal_phonemes(gentle_data, FRAME_PER_SECOUND=24, EXTRA_TIME=0):
    print("adding normal phrases")
    if gentle_data.get("words"):
        gentle_length = len(gentle_data["words"])
        FRAME_PER_SECOUND = FRAME_PER_SECOUND
        # AUDO_END_TIME = gentle_data["words"][-1]["end"]
        AUDO_END_TIME = gentle_data["words"][-1].get("end")
        print("AUDO_END_TIME :",AUDO_END_TIME)
        counter = -1
        while not AUDO_END_TIME:
            print(AUDO_END_TIME)
            counter -=  1
            AUDO_END_TIME = gentle_data["words"][counter].get("end")
        EXTRA_TIME = EXTRA_TIME
        AUDO_END_TIME = math.ceil(float(AUDO_END_TIME) + EXTRA_TIME)
        for counter in range(gentle_length):
            each_data = gentle_data["words"][counter]
            # "case": "success",
            if each_data["case"] == "success":
                each_data["init_frame"] = math.ceil(
                    float(each_data["start"]) * FRAME_PER_SECOUND
                )
                each_data["final_frame"] = math.ceil(
                    float(each_data["end"]) * FRAME_PER_SECOUND
                )

                each_data["diff"] = math.ceil(
                    (each_data["final_frame"] - each_data["init_frame"])
                )

                each_data["phonemes"] = g2p(each_data["word"])
                print(each_data["phonemes"])
                dic_ = {}
                for each_phone in each_data["phonemes"]:
                    dic_[each_phone] = 0
                    each_data["phonemes_frame"] = dic_
                each_data["phonemes_frame"] = equalizer(
                    each_data["diff"], each_data["phonemes_frame"]
                )
            else:
                each_data["init_frame"] = -1
                each_data["final_frame"] = -1

        gentle_data["FRAME_PER_SECOUND"] = FRAME_PER_SECOUND
        gentle_data["AUDO_END_TIME"] = AUDO_END_TIME
        gentle_data["TOTAL_VIDEO_FRAMES"] = AUDO_END_TIME * FRAME_PER_SECOUND + 1
        gentle_data["MODE"] = "normal"

    return gentle_data


def add_gentle_phonemes(gentle_data, FRAME_PER_SECOUND=24, EXTRA_TIME=0):
    gentle_length = len(gentle_data["words"])
    FRAME_PER_SECOUND = FRAME_PER_SECOUND
    AUDO_END_TIME = gentle_data["words"][-1]["end"]
    EXTRA_TIME = EXTRA_TIME
    AUDO_END_TIME = math.ceil(float(AUDO_END_TIME) + EXTRA_TIME)
    for counter in range(gentle_length):
        each_data = gentle_data["words"][counter]
        # "case": "success",
        if each_data["case"] == "success":
            each_data["init_frame"] = math.ceil(
                float(each_data["start"]) * FRAME_PER_SECOUND
            )
            each_data["final_frame"] = math.ceil(
                float(each_data["end"]) * FRAME_PER_SECOUND
            )

            each_data["diff"] = math.ceil(
                (each_data["final_frame"] - each_data["init_frame"])
            )
            # "phonemes_frame": { "K": 2, "EH1": 2, "R": 2 }
            phones = each_data.get("phones")
            if phones:
                dic_ = {}
                for each_phone in phones:
                    dic_[each_phone["phone"]] = math.ceil(
                        float(each_phone["duration"]) * FRAME_PER_SECOUND
                    )
                each_data["phonemes_frame"] = dic_
                each_data["phonemes_frame"] = equalizer(
                    each_data["diff"], each_data["phonemes_frame"]
                )
        else:
            each_data["init_frame"] = -1
            each_data["final_frame"] = -1

    gentle_data["FRAME_PER_SECOUND"] = FRAME_PER_SECOUND
    gentle_data["AUDO_END_TIME"] = AUDO_END_TIME
    gentle_data["TOTAL_VIDEO_FRAMES"] = AUDO_END_TIME * FRAME_PER_SECOUND + 1
    gentle_data["MODE"] = "gentle"

    return gentle_data


def edit_image_list(image_list):
    # first check

    for counter, each_image in enumerate(image_list[1:-1]):
        if (
            image_list[counter] != each_image
            and image_list[counter] == image_list[counter + 2]
        ):
            image_list[counter + 1] = image_list[counter]
    return image_list


def framer_reader(gentle_data, folder_name="happy"):
    # C:\Users\cacf\Documents\website_work\lipsync
    path = str(basepath).replace("\\", "/")

    frame_counter = 0
    # if gentle_data['MODE'] == 'gentle':
    #     f = open('./json/gentle_phonemes.json')
    # else:
    #     f = open('./json/phonemes_json.json')

    # phonemes = json.load(f)
    phonemes = NORMAL_PHONEMES
    images_list = []
    # print(phonemes)
    while frame_counter <= gentle_data["TOTAL_VIDEO_FRAMES"]:

        for each_fagment in gentle_data["words"]:
            # print(each_fagment['init_frame'])
            if (
                frame_counter >= each_fagment["init_frame"]
                and frame_counter <= each_fagment["final_frame"]
            ):
                # print(frame_counter, ' and  ',each_fagment['init_frame'] )

                for phoneme, number_of_frame in each_fagment["phonemes_frame"].items():
                    # print(phoneme)
                    if phonemes.get(phoneme):
                        # print('found')
                        phonem_dic = phonemes.get(phoneme)
                        for number in range(int(number_of_frame)):
                            image_name = phonem_dic["happy"]
                            print(image_name)
                            images_list.append(
                                path
                                + "/media/images/{0}/{1}".format(
                                    folder_name, image_name
                                )
                            )
                            frame_counter += 1

        mouth_path = path + "/media/images/{0}/m_b_close_h.png".format(folder_name)
        images_list.append(mouth_path)

        print(mouth_path)
        frame_counter += 1
    if gentle_data["MODE"] == "gentle":
        return edit_image_list(images_list)
    else:
        return images_list


def frame_creater(image_list):
    path = str(basepath).replace("\\", "/")
    bg_path = path + "/media/images/background/greenbg.png"
    bg = Image.open(bg_path)

    bg_name = bg_path.split("/")[-1].split(".")[0]

    frame_data = {"key_counter": {}, "frame_key": {}}
    mypath = path + "/media/frames"
    files = [f for f in os.listdir(mypath)]
    for each_file in files:
        key_name = each_file.split(".")[0]
        if key_name:
            frame_data["key_counter"][each_file.split(".")[0]] = 1

    for counter, each_lip_path in enumerate(image_list):
        lip_name = each_lip_path.split("/")[-1].split(".")[0]
        folder_name = each_lip_path.split("/")[-2]
        key = bg_name + lip_name + folder_name
        if key not in frame_data["key_counter"]:
            frame_data["key_counter"][key] = 1
            image = None
            lip = Image.open(each_lip_path)
            bg = Image.open(bg_path)
            image = adding_image(bg, lip, location=(200, 250))
            print(counter)
            image.save(path + "/media/frames/{0}.png".format(key))
        else:
            frame_data["key_counter"][key] = frame_data["key_counter"][key] + 1
        frame_data["frame_key"][counter] = key

    with open(
        path + "/common/frameCreationInfo/frameCreationInfo.json", "w"
    ) as outfile:
        json.dump(frame_data, outfile)

    return frame_data

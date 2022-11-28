import time
from .models import GentleJson, File


def hook_funcs(task):
    print("yes save the json")
    print("type --------------------", type(task.result.get('gentle_data')))
    file = File.objects.get(id=task.result.get('file_id'))
    GentleJson.objects.create(file=file, json=task.result.get('gentle_data'))

    print("The result is done for : ", task.result.get('file_id'))


def sleepy_func(junk,sleep):
    print("sleep: ",sleep* junk )
    for i in range(10):
        print("hello ", i)
        time.sleep(1)
    print ("sleepy function ran")

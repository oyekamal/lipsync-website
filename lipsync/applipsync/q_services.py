import time
from .models import GentleJson


def hook_funcs(task):
    # GentleJson.objects.create()
    print("The result is done for : ", task.result.get('file_id'))


def sleepy_func(junk,sleep):
    print("sleep: ",sleep* junk )
    for i in range(10):
        print("hello ", i)
        time.sleep(1)
    print ("sleepy function ran")

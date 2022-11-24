import time



def hook_funcs(task):

    print("The task result is: ", task.result)


def sleepy_func(junk,sleep):
    print("sleep: ",sleep* junk )
    for i in range(10):
        print("hello ", i)
        time.sleep(1)
    print ("sleepy function ran")

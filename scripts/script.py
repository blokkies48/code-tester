
from threading import Thread
import time
import os

thread:Thread = None

def thread_code():
    time.sleep(10)
    os.kill(os.getpid(), 9)

def func():
    thread = Thread(target=thread_code)
    thread.daemon = True
    thread.start()
func()

str_1 = ""
for i in range(100000000):
    str_1 += "1"

exit()

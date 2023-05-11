
from threading import Thread
import time
import os

from shared import *

thread:Thread = None

def thread_code():
    time.sleep(10)
    os.kill(os.getpid(), 9)

def func():
    thread = Thread(target=thread_code)
    thread.daemon = True
    thread.start()
func()



for i in range(value):
	num_1 += i
	



exit()

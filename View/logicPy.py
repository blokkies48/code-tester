import subprocess
import time
from Models.UI_model import UI_tk
from threading import Thread

TEMP = """
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
{}
{}

exit()
"""

class BaseProgram:
    has_thread = False
    process:subprocess = None
    output_message = list()
    is_cancelled = False

class TheProcesses(BaseProgram):
    def run_script(self, cmd):
        try:
            self.process = subprocess.Popen(cmd, shell=True)       
            self.process.communicate()
        except:
            pass
        
    def check_time_script(self, file:str):

        # Test script 1
        start_time = time.time()

        cmd = f"python scripts\\{file}"
        self.run_script(cmd)

        end_time = time.time()
        time_1 = end_time - start_time

        return time_1
    
    def get_input(self, screen:UI_tk):
        self.output_message = list()

        directory = "scripts"

        list_name = ['script.py', 'script_2.py']

        screen.lbl.config(text = "")
        screen.lbl_status.config(text = f"Processing...")

        inputs= list(screen.get_text_inputs())
        shared_variables:str = ''

        with open(f'{directory}\\shared.py', 'w') as shared:
            shared.write(inputs[2].get(1.0, "end-1c"))

        def main_scripts():
            for index, filename in enumerate(list_name):

                inp = inputs[index].get(1.0, "end-1c")
                with open(f"{directory}\\{filename}", "w") as f1:
                    f1.write(TEMP.format(shared_variables, inp))

                self.is_cancelled = False
                time_1 = self.check_time_script(filename)

                if time_1 > 10 and not self.is_cancelled:
                    self.output_message.append(f"Timed out")
                elif not self.is_cancelled:
                    self.output_message.append(f"Timed")

                self.output_message.append(f"time {index + 1}: {time_1}")
                screen.lbl.config(text = "\n".join(self.output_message))
            self.is_running = False

            screen.lbl_status.config(text = f"Done!")

            self.has_thread = False
        main_scripts()

class TheButtons(BaseProgram):
    def run_thread(self, screen:UI_tk):
        if not self.has_thread:
            self.is_running = True

            thread = Thread(target=self.get_input, args=(screen,))
            thread.daemon = True
            thread.start()

            self.has_thread = True
        else:
            screen.lbl_status.config(text="Please wait processing...")


    def reset_all(self, screen:UI_tk):
        if not self.has_thread:
            screen.lbl.config(text="")
            screen.lbl_status.config(text="") 
            screen.clear_text_boxes()

    def reset_time (self, screen:UI_tk):
        if not self.has_thread:
            screen.lbl.config(text="")
            screen.lbl_status.config(text="") 

    def cancel(self):
        if self.has_thread:
            try:
                self.process.terminate()
                self.process.wait()
                self.output_message.append("Cancelled")
                self.is_cancelled = True
            except:
                pass

class ProgramPython(TheProcesses, TheButtons):
    
    def __init__(self, UI:UI_tk):
        self.UI = UI
        
    def run(self):   
        screen:UI_tk = self.UI

        screen.button_run(lambda: self.run_thread(screen))
        screen.button_reset_all(lambda: self.reset_all(screen))
        screen.button_reset_time(lambda: self.reset_all(screen))
        screen.cancel_process(lambda: self.cancel())

        screen.run()
    
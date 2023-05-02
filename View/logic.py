import subprocess
import time

def clean_files():
    # Clean up script files:
    with open("scripts\\script.py", "w") as f2:
        f2.write("")

    with open("scripts\\script_2.py", "w") as f2:
        f2.write("")

def run_script(cmd):
    process= subprocess.Popen(cmd, shell=True)
    process.communicate()

def check_time_script(file:str):
    # Test script 1
    start_time = time.time()

    cmd = f"python scripts\\{file}"
    run_script(cmd)

    end_time = time.time()
    # print(end_time - start_time)

    time_1 = end_time - start_time

    return time_1

from Models.UI_model import UI_tk


from threading import Thread
import os

class Program:
    has_thread = False

    def get_input(self, screen:UI_tk):

        clean_files()

        output_message = list()
        directory = "scripts"

        screen.lbl.config(text = "")
        screen.lbl_status.config(text = f"Processing...")

        inputs= list(screen.get_text_inputs())

        for index, filename in enumerate(os.listdir(directory)):

            inp = inputs[index].get(1.0, "end-1c")
            with open(f"{directory}\\{filename}", "w") as f1:
                f1.write(inp)

            time_1 = check_time_script(filename)
            output_message.append(f"time {index + 1}: {time_1}")
            screen.lbl.config(text = "\n".join(output_message))
        
        screen.lbl_status.config(text = f"Done!")

        self.has_thread = False

    def run_thread(self, screen:UI_tk):
        if not self.has_thread:
            thread = Thread(target=self.get_input, args=(screen,))
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


    def run(self):   
        screen = UI_tk("Please note syntax isn't checked and can affect result.\nCopy past python code and compare.")

        
        screen.button_run(self.run_thread, is_lambda=True, arg=screen)
        screen.button_reset_all(self.reset_all, is_lambda=True, arg=screen)
        screen.button_reset_time(self.reset_time, is_lambda=True, arg=screen)

        screen.run()
    
from Models.UI_model import UI_tk
from View.logic import * 

from threading import Thread
import os

def get_input(screen:UI_tk):

    clean_files()

    output_message = list()
    directory = "scripts"

    screen.lbl.config(text = "")
    screen.lbl_status.config(text = f"Processing...")

    inputs= list(screen.get_text_inputs())

    count = 1

    for index, filename in enumerate(os.listdir(directory)):
        print(filename)

        inp = inputs[index].get(1.0, "end-1c")
        with open(f"{directory}\\{filename}", "w") as f1:
            f1.write(inp)

        time_1 = check_time_script(filename)
        output_message.append(f"time {index + 1}: {time_1}")
        screen.lbl.config(text = "\n".join(output_message))
        count += 1
    
    screen.lbl_status.config(text = f"Done!")


def run_thread(screen:UI_tk):
    
    thread = Thread(target=get_input, args=(screen,))
    thread.start()    

def main():   
    screen = UI_tk("Please note syntax isn't checked and can affect result.\nCopy past python code and compare.")

    screen.button_run(run_thread, is_lambda=True, arg=screen)

    screen.run()
    
main()
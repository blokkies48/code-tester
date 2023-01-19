

import subprocess
import time
# Testing the 2 blocks algorithm
def check_time():
    # Test script 1
    start_time = time.time()

    cmd = "python script.py"
    p= subprocess.Popen(cmd, shell=True)

    end_time = time.time()
    print(end_time - start_time)

    time_1 = end_time - start_time

    # Test script 2
    start_time = time.time()

    cmd = "python script_2.py"
    p= subprocess.Popen(cmd, shell=True)

    end_time = time.time()
    time_2 = end_time - start_time
    print(end_time - start_time)

    return time_1, time_2


# App interface

import tkinter as tk
  
# Top level window

frame = tk.Tk()
frame.title("TextBox Input")

# logic for running
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    with open("script.py", "w") as f2:
        f2.write(inp)

    inp_2 = inputtxt_2.get(1.0, "end-1c")
    with open("script_2.py", "w") as f2:
        f2.write(inp_2)

    times = check_time()
    fastest = ''
    if times[0] < times[1]:
        fastest = "First code is the fastest"
    else:
        fastest = "Second code is the fastest"
    lbl.config(text = f"First Time: {times[0]}\nSecond Time {times[1]}\n {fastest}" )
    
# UI
lbl_1 = tk.Label(frame, text = "Please note syntax isn't checked and can affect result.\nCopy past python code and compare.")
lbl_1.pack()
  
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 15,
                   width = 60)

inputtxt_2 = tk.Text(frame,
                   height = 15,
                   width = 60)
  
inputtxt.pack()
inputtxt_2.pack()
  
# Button Creation
printButton = tk.Button(frame,
                        text = "Run", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
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
    print(end_time - start_time)

    time_1 = end_time - start_time

    return time_1
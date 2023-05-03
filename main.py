from View.logicPy import ProgramPython
from Models.UI_model import UI_tk

def main():
    UI = UI_tk(
        "Please note syntax isn't checked and can affect result.\nCopy past python code and compare.")
    
    ProgramPython(UI).run()

if __name__ == '__main__':
    main()
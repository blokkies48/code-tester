import tkinter as tk

class UI_tk:
    frame = tk.Tk()
    frame.title("TextBox Input")

    def __init__(self, top_label):
        lbl_1 = tk.Label(self.frame, text=top_label)
        lbl_1.pack()
        
        # TextBox Creation
        self.text_input_1 = tk.Text(self.frame,
                        height = 15,
                        width = 60)

        self.text_input_2 = tk.Text(self.frame,
                        height = 15,
                        width = 60)
        
        self.text_input_1.pack()
        self.text_input_2.pack()
        
        # Label Creation
        self.lbl = tk.Label(self.frame, text = "")
        self.lbl.pack()
        
        self.lbl_status = tk.Label(self.frame, text = "")
        self.lbl_status.pack()

    def button_run(self, command, is_lambda=False, arg=None):
        if is_lambda:
            printButton = tk.Button(self.frame,
                                text="Run", 
                                command=lambda: command(arg))
        else:
            printButton = tk.Button(self.frame,
                                text="Run", 
                                command=command)
        printButton.pack()

    def get_text_inputs(self):
        return self.text_input_1, self.text_input_2

    def run(self):
        self.frame.mainloop()


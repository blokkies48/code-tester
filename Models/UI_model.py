import tkinter as tk
class __UI_buttons:

    WIDTH = 10
    HEIGHT = 2
    PADX = 10
    PADY = 5
    SIDE = 'left'

    def button_run(self, command, is_lambda=False, arg=None):
        if is_lambda:
            print_button = tk.Button(self.frame,
                                text="Run", 
                                command=lambda: command(arg),
                                width=self.WIDTH, height=self.HEIGHT)
        else:
            print_button = tk.Button(self.frame,
                                text="Run", 
                                command=command,
                                width=self.WIDTH, height=self.HEIGHT)
        print_button.pack(padx=self.PADX, pady=self.PADY, side=self.SIDE)

    def button_reset_all(self, command, is_lambda=False, arg=None):
        if is_lambda:
            button = tk.Button(self.frame,
                                text="Reset All", 
                                command=lambda: command(arg),
                                width=self.WIDTH, height=self.HEIGHT)
        else:
            button = tk.Button(self.frame,
                                text="Reset All", 
                                command=command,
                                width=self.WIDTH, height=self.HEIGHT)
        button.pack(padx=self.PADX, pady=self.PADY, side=self.SIDE)

    def button_reset_time(self, command, is_lambda=False, arg=None):
        if is_lambda:
            button = tk.Button(self.frame,
                                text="Reset Time", 
                                command=lambda: command(arg),
                                width=self.WIDTH, height=self.HEIGHT)
        else:
            button = tk.Button(self.frame,
                                text="Reset Time", 
                                command=command,
                                width=self.WIDTH, height=self.HEIGHT)
        button.pack(padx=self.PADX, pady=self.PADY, side=self.SIDE)

    def cancel_process(self, command, is_lambda=False, arg=None):
        if is_lambda:
            button = tk.Button(self.frame,
                                text="Cancel", 
                                command=lambda: command(arg),
                                width=self.WIDTH, height=self.HEIGHT)
        else:
            button = tk.Button(self.frame,
                                text="Cancel", 
                                command=command,
                                width=self.WIDTH, height=self.HEIGHT)
        button.pack(padx=self.PADX, pady=self.PADY, side='right')


class UI_tk(__UI_buttons):
    frame = tk.Tk()
    frame.title("Code Tester 3000")

    TEXT_HEIGHT = 20
    TEXT_WIDTH = 70

    def __init__(self, top_label):
        lbl_1 = tk.Label(self.frame, text=top_label)
        lbl_1.pack()
        
        # TextBox Creation
        self.text_input_1 = tk.Text(self.frame,
                        height = self.TEXT_HEIGHT,
                        width = self.TEXT_WIDTH)

        self.text_input_2 = tk.Text(self.frame,
                        height = self.TEXT_HEIGHT,
                        width = self.TEXT_WIDTH)
        
        self.text_input_1.pack()
        self.text_input_2.pack()
        
        # Label Creation
        self.lbl = tk.Label(self.frame, text = "")
        self.lbl.pack()
        
        self.lbl_status = tk.Label(self.frame, text = "")
        self.lbl_status.pack()

    def get_text_inputs(self):
        return self.text_input_1, self.text_input_2
    
    def clear_text_boxes(self):
        self.text_input_1.delete('1.0',tk.END)
        self.text_input_2.delete('1.0',tk.END)

    def run(self):
        self.frame.mainloop()


import math
import tkinter as tk
from tkinter import messagebox

# Calculator logic
class SciCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display frame
        input_frame = tk.Frame(master, bd=2, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP, fill="both")

        input_field = tk.Entry(input_frame, textvariable=self.input_text,
                               font=('Arial', 18), bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0, ipady=10, padx=5, pady=5)

        # Buttons frame
        btns_frame = tk.Frame(master)
        btns_frame.pack()

        # Button layout
        buttons = [
            ('7', '8', '9', '/', 'sin'),
            ('4', '5', '6', '*', 'cos'),
            ('1', '2', '3', '-', 'tan'),
            ('0', '.', '%', '+', 'log'),
            ('(', ')', '√', '^', 'ln'),
            ('C', '⌫', '=', )
        ]

        # Create buttons
        for r, row in enumerate(buttons):
            for c, btn_text in enumerate(row):
                btn = tk.Button(btns_frame, text=btn_text, width=5, height=2,
                                font=('Arial', 14),
                                command=lambda x=btn_text: self.on_button_click(x))
                btn.grid(row=r, column=c, padx=2, pady=2)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == '=':
            try:
                # Replace special symbols
                expr = self.expression.replace('^', '**').replace('√', 'math.sqrt')
                result = eval(expr, {"math": math, "__builtins__": {}})
                self.input_text.set(str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
                self.input_text.set("")
        elif char in ('sin', 'cos', 'tan', 'log', 'ln'):
            try:
                val = float(self.expression)
                if char == 'sin':
                    res = math.sin(math.radians(val))
                elif char == 'cos':
                    res = math.cos(math.radians(val))
                elif char == 'tan':
                    res = math.tan(math.radians(val))
                elif char == 'log':
                    res = math.log10(val)
                else:  # ln
                    res = math.log(val)
                self.input_text.set(str(res))
                self.expression = str(res)
            except Exception:
                messagebox.showerror("Error", "Invalid Input for function")
                self.expression = ""
                self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = SciCalculator(root)
    root.mainloop()

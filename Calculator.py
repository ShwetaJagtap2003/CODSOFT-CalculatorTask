import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        self.expression = ""
        self.result_var = tk.StringVar(value="0")
        
        # Create display
        display_frame = tk.Frame(root)
        display_frame.pack(pady=10)
        
        self.display = tk.Entry(display_frame, textvariable=self.result_var, 
                               font=('Arial', 20), justify='right', bd=10, relief=tk.RIDGE)
        self.display.pack()
        
        # Create buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                color = '#4CAF50' if text == '=' else ('#2196F3' if text in '/*-+' else '#f0f0f0')
                btn = tk.Button(button_frame, text=text, font=('Arial', 14), width=5, height=2,
                               bg=color, command=lambda t=text: self.button_click(t))
                btn.grid(row=i, column=j, padx=2, pady=2)
        
        # Clear buttons
        clear_frame = tk.Frame(root)
        clear_frame.pack()
        tk.Button(clear_frame, text='C', font=('Arial', 14), width=11, height=2,
                 bg='#f44336', command=self.clear).pack(side=tk.LEFT, padx=2)
        tk.Button(clear_frame, text='⌫', font=('Arial', 14), width=11, height=2,
                 bg='#FF9800', command=self.backspace).pack(side=tk.LEFT, padx=2)
    
    def button_click(self, button_text):
        current = self.result_var.get()
        
        if button_text == '=':
            try:
                result = eval(current)
                self.result_var.set(str(result))
            except:
                messagebox.showerror("Error", "Invalid Calculation")
                self.clear()
        elif button_text == 'C':
            self.clear()
        else:
            if current == '0' or current == 'Error':
                self.result_var.set(button_text)
            else:
                self.result_var.set(current + button_text)
    
    def clear(self):
        self.result_var.set("0")
    
    def backspace(self):
        current = self.result_var.get()
        if len(current) > 1:
            self.result_var.set(current[:-1])
        else:
            self.result_var.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
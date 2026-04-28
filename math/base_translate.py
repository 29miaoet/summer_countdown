import tkinter as tk

hex_digits=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]


def validate_positive(new_value):
    if new_value == "":
        return True
    try:
        return float(new_value) > 0
    except ValueError:
        return False

def translate_base(base):
    try:
        num = int(inputfield.get("1.0", "end-1c"))
        outputfield.config(state="normal")
        outputfield.delete("1.0",tk.END)
        outputfield.config(state="disabled")
        if base == 1:
            digits = [1 for i in range(num)]
            
        else:
            digits = []

            if num == 0:
                digits.append(0)
            else:
                while num > 0:
                    num, remainder = divmod(num, base)
                    digits.append(remainder)

            digits.reverse()
        outputstring = ""
        if base == 16:
            for digit in digits:
                outputstring += hex_digits[digit]
        elif base == 60:
            for digit in digits:
                outputstring += str(digit)
                if digit is not digits[-1]:
                    outputstring += ":"
        elif base <= 10:
            for digit in digits:
                outputstring += str(digit)
        else:
            for digit in digits:
                outputstring += str(digit)
                outputstring += " "
        
        outputfield.config(state="normal")
        outputfield.insert("1.0", outputstring)
        outputfield.config(state="disabled")
    except ValueError:
        outputfield.config(state="normal")
        outputfield.delete("1.0",tk.END)
        outputfield.insert("1.0", "please enter a valid number")
        outputfield.config(state="disabled")

def validate_custom_base_button():
    try:
        translate_base(int(base.get()))
    except ValueError:
        outputfield.config(state="normal")
        outputfield.delete("1.0",tk.END)
        outputfield.insert("1.0", "please enter a valid custom base")
        outputfield.config(state="disabled")

menu=tk.Tk()
menu.title("Base Translator")
menu.grid_rowconfigure([0,1,2,3,4,5], weight=1)
menu.grid_columnconfigure([0,1,2], weight=1)

vcmd = (menu.register(validate_positive), "%P")
base = tk.Entry(menu, validate="key", validatecommand=vcmd)
basebutton = tk.Button(menu, text="Custom Base", relief=tk.GROOVE, command=validate_custom_base_button)

inputfield = tk.Text(menu, height=10)
outputfield = tk.Text(menu, height=10)
outputfield.config(state="disabled")

translate_bin = tk.Button(menu, text="Binary", relief=tk.GROOVE, command=lambda: translate_base(2))
translate_hex = tk.Button(menu, text="Hex", relief=tk.GROOVE, command=lambda: translate_base(16))
translate_oct = tk.Button(menu, text="Oct", relief=tk.GROOVE, command=lambda: translate_base(8))
translate_cvmn = tk.Button(menu, text="Caveman", relief=tk.GROOVE, command=lambda: translate_base(1))
translate_bs60 = tk.Button(menu, text="Base60", relief=tk.GROOVE, command=lambda: translate_base(60))

translate_bin.grid(row=0, column=0, columnspan=2, sticky="nsew")
translate_hex.grid(row=1, column=0, columnspan=2, sticky="nsew")
translate_oct.grid(row=2, column=0, columnspan=2, sticky="nsew")
translate_cvmn.grid(row=3, column=0, columnspan=2, sticky="nsew")
translate_bs60.grid(row=4, column=0, columnspan=2, sticky="nsew")
base.grid(row=5, column=0, sticky="nsew")
basebutton.grid(row=5, column=1, sticky="nsew")
inputfield.grid(row=0, column=2, rowspan=3, sticky="nsew")
outputfield.grid(row=3, column=2, rowspan=3, sticky="nsew")

menu.mainloop()


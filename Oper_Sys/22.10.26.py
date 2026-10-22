import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("320x450")

expression = ""

# Пункт 5
text_input = tk.Label(root, text="", font=('Arial', 16), bg="lightgray", anchor="e", width=22)
text_input.grid(row=0, column=0, columnspan=5, pady=5)

text_result = tk.Label(root, text="", font=('Arial', 16), bg="white", anchor="e", width=22)
text_result.grid(row=1, column=0, columnspan=5, pady=5)

# Пункт 6
def multiply():
    global expression
    text_result.config(text=eval(expression))
    expression = ""

def divide():
    global expression
    text_result.config(text=eval(expression))
    expression = ""

def summy():
    global expression
    text_result.config(text=eval(expression))
    expression = ""

def diff():
    global expression
    text_result.config(text=eval(expression))
    expression = ""

def result():
    global expression
    text_result.config(text=eval(expression))
    expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    text_input.config(text=expression)

# Пункт 2
numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
row_num = 2
col_num = 0

for num in numbers:
    btn = tk.Button(root, text=num, width=5, height=2, command=lambda n=num: press(n))
    btn.grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1

# Пункт 3
operations_matrix = [
    ("multiply", "*", multiply),
    ("divide", "%", divide),
    ("summy", "+", summy),
    ("diff", "-", diff),
    ("result", "=", result)
]

# Пункт 4
op_row = 2
for name, symbol, func in operations_matrix:
    btn = tk.Button(root, text=symbol, width=5, height=2, command=func)
    btn.grid(row=op_row, column=3)
    op_row += 1

def clear():
    global expression
    expression = ""
    text_input.config(text="")
    text_result.config(text="")

tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=5, column=2)

root.mainloop()
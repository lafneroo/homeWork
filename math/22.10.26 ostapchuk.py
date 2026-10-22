import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x450")

# Переменная для хранения введенного текста
expression = ""

# 5. Поле для ввода (сверху)
text_input = tk.Label(root, text="", font=('Arial', 16), bg="lightgray", anchor="e", width=20)
text_input.grid(row=0, column=0, columnspan=5, pady=5)

# 6. Поле для результата (под вводом)
text_result = tk.Label(root, text="", font=('Arial', 16), bg="white", anchor="e", width=20)
text_result.grid(row=1, column=0, columnspan=5, pady=5)


# Функция для нажатия на цифры
def press(num):
    global expression
    expression = expression + str(num)
    text_input.config(text=expression)


# 6. Пять функций для операций
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


# 2. Кнопки с цифрами 0-9 через цикл for
# Список цифр в порядке расположения на клавиатуре
numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']

row = 2
col = 0
for num in numbers:
    # Создаем кнопку. Используем lambda, чтобы запомнить текущую цифру
    btn = tk.Button(root, text=num, width=5, height=2, command=lambda n=num: press(n))
    btn.grid(row=row, column=col)

    col = col + 1
    if col > 2:  # После 3-х кнопок в ряду переходим на новую строку
        col = 0
        row = row + 1

# 3. Матрица (список) для операций
operations = [
    ("multiply", "*", multiply),
    ("divide", "%", divide),
    ("summy", "+", summy),
    ("diff", "-", diff),
    ("result", "=", result)
]

# 4. Кнопки для операций через цикл for
row_num = 2
for name, symbol, func in operations:
    btn = tk.Button(root, text=symbol, width=5, height=2, command=func)
    btn.grid(row=row_num, column=3)  # 4-й столбец
    row_num = row_num + 1


# Кнопка очистки
def clear():
    global expression
    expression = ""
    text_input.config(text="")
    text_result.config(text="")


tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=5, column=2)

# Запуск программы
root.mainloop()
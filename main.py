import tkinter as tk

def calculate(operation):
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    label.config(text = "Результат: " + str(result))

window = tk.Tk()
window.title("Калькулятор")

entry1 = tk.Entry(window, width=10)
entry1.grid(row=0, column=0)

entry2 = tk.Entry(window, width=10)
entry2.grid(row=0, column=1)

operations = ['+', '-', '*', '/', 'Рассчитать']
for i, operation in enumerate(operations):
    button = tk.Button(window, text=operation, command=lambda operation=operation: calculate(operation))
    button.grid(row=1, column=i)

label = tk.Label(window, text="Результат: ")
label.grid(row=2, column=0, columnspan=5)

window.mainloop()

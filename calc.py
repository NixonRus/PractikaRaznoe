import tkinter as tk

def get_values():
    numb1 = int(number1_entry.get())
    numb2 = int(number2_entry.get())
    return numb1, numb2

def insert_values(values):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, values)

def add():
    numb1, numb2 = get_values()
    res = numb1 + numb2
    insert_values(res)

def sub():
    numb1, numb2 = get_values()
    res = numb1 - numb2
    insert_values(res)

def mul():
    numb1, numb2 = get_values()
    res = numb1 * numb2
    insert_values(res)

def dev():
    numb1, numb2 = get_values()
    res = numb1 / numb2
    insert_values(res)

window = tk.Tk()
window.title('Калькулятор "Косметик"')
window.geometry('400x400')
window.resizable(False, False)
window.config(bg='#1C1C1C')

button_add = tk.Button(window, text='+', font='Times 10 bold', width=4, height=3, command=add)
button_add.place(x=90, y=180)
button_add.config(bg='#D71868')
button_sub = tk.Button(window, text='-', font='Times 10 bold', width=4, height=3, command=sub)
button_sub.place(x=155, y=180)
button_sub.config(bg='#D71868')
button_mul = tk.Button(window, text='*', font='Times 10 bold', width=4, height=3, command=mul)
button_mul.place(x=220, y=180)
button_mul.config(bg='#D71868')
button_dev = tk.Button(window, text='/', font='Times 10 bold', width=4, height=3, command=dev)
button_dev.place(x=285, y=180)
button_dev.config(bg='#D71868')
number1_entry = tk.Entry(window, width=38, font='Times 9 bold')
number1_entry.place(x=90, y=50)
number2_entry = tk.Entry(window, width=38, font='Times 9 bold')
number2_entry.place(x=90, y=120)
answer_entry = tk.Entry(window, width=38, font='Times 9 bold')
answer_entry.place(x=90, y=290)
number1 = tk.Label(window, text='Введите первое число:', font='Times 12 bold italic', fg='#D71868')
number1.place(x=90, y=25)
number1.config(bg='#1C1C1C')
number2 = tk.Label(window, text='Введите второе число:', font='Times 12 bold italic', fg='#D71868')
number2.place(x=90, y=95)
number2.config(bg='#1C1C1C')
answer = tk.Label(window, text='Ответ:', font='Times 12 bold italic', fg='#D71868')
answer.place(x=90, y=265)
answer.config(bg='#1C1C1C')

window.mainloop()

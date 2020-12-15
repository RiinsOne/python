import tkinter as tk

window = tk.Tk()

data = tk.StringVar()
# Создаем объект класса StringVar и присваиваем указатель на него data
# (создаем строковую переменную, с которой умеет работать tkinter)

# Tkinter поддерживает работу с переменными классов: BooleanVar, DoubleVar, IntVar, StringVar

data.set('Данные в окне')
# Метод set класса StringVar позволяет изменить содержимое переменной

label = tk.Label(window, textvariable=data)
# textvariable присваиваем ссылку на строковый объект из переменной data
label.pack()

window.mainloop()













#

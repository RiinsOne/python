import tkinter as tk

window = tk.Tk()
frame = tk.Frame(window, borderwidth=50)
frame.pack()

var = tk.StringVar()

label = tk.Label(frame, textvariable=var)
label.pack()
# Обновление содержимого переменной происходит в режиме реального времени

entry = tk.Entry(frame, textvariable=var)
entry.pack()

window.mainloop()

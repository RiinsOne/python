import tkinter as tk

window = tk.Tk()

frame = tk.Frame(window)
# Создаем фрейм в главном окне
frame.pack()

frame2 = tk.Frame(window, borderwidth=4, relief=tk.GROOVE)
frame2.pack()
# Можно изменять параметры фрейма

first = tk.Label(frame, text='First label')
# Создаем виджеты и помещаем их во фрейме frame
first.pack()

second = tk.Label(frame2, text='Second label')
# размещаем виджеты во втором фрейме (frame2)
second.pack()

third = tk.Label(frame2, text='Third label')
third.pack()



window.mainloop()







#

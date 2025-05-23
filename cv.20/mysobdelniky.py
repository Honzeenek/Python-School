import tkinter
import random

canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

def klik(mys):
    barvy = ['red', 'yellow', 'green', 'blue']
    canvas.create_rectangle(10, 10, mys.x, mys.y, fill=random.choice(barvy))
def smaz(mys):
    canvas.delete('all')

canvas.bind('<B1-Motion>', klik)
canvas.bind('<ButtonPress-3>', smaz)
canvas.mainloop()
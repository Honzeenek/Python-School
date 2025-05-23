import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def klik(mys):  
    canvas.bind('<B1-Motion>', klik)
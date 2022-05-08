import random
from PIL import Image, ImageTk
from tkinter import Label, Pack, Button, Tk

rt = Tk()
rt.geometry("600x600")
rt.title("Python Dice Roller")

a = Label(rt, font = ('Helvetica', 280), text = '')

def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    a.configure(text = f'{random.choice(dice)}')
    a.pack()

do = Button(rt, text = 'Roll a die', command = roll)
do.pack()
Cb = Button(rt, text = 'Close', command = lambda: rt.destroy())
Cb.pack()
rt.mainloop()
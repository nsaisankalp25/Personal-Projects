from tkinter import Label,Tk 
from PIL import Image, ImageTk

rt = Tk()

load = ImageTk.PhotoImage(Image.open('icon.png'))
imgl = Label(rt, image = load).pack()

rt.mainloop()
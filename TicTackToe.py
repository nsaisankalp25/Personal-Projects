from tkinter import *
w, tries, board = [0], [], {}
for i in range(1, 9):board[i] = " "
rt = Tk()
rt.geometry("500x500")

def game_over(xo):
    for win in rt.winfo_children(): win.destroy()
    if xo != False: Label(rt, text = f"{xo} Wins!", font = ('montserrat', 30), fg = 'green').pack()
    else:Label(rt, text = "Game Over. TIE", font = ('montserrat', 30), fg = 'red').pack()

def main_def(num: str):
    try:
        if w[0] == 1:
            try:    
                exec(f"{num}.config(text = 'X', state = DISABLED)")
                w[0] = 0
                board[int(num.replace('b', ''))] = 'X'
                tries.append(0)
                main_def("a")
            except: pass
        else:
            try:
                exec(f"{num}.config(text = 'O', state = DISABLED)")
                w[0] = 1
                board[int(num.replace('b', ''))] = 'O'
                tries.append(0)
                main_def('a')
            except: pass
        if b1['text'] == b5['text'] == b9['text'] != " ":
            print(f"{b1['text']} Wins!")
            game_over(b1['text'])

        elif b1['text'] == b2['text'] == b3['text'] != " ":
            print(f"{b1['text']} Wins!")
            game_over(b1['text'])

        elif b1['text'] == b4['text'] == b7['text'] != " ":
            print(f"{b1['text']} Wins!")

        elif b2['text'] == b5['text'] == b8['text'] != " ":
            print(f"{b2['text']} Wins!")
            game_over(b2['text'])

        elif b5['text'] == b4['text'] == b6['text'] != " ":
            print(f"{b5['text']} Wins!")
            game_over(b5['text'])
        
        elif b7['text'] == b8['text'] == b9['text'] != " ":
            print(f"{b7['text']} Wins!")
            game_over(b7['text'])
        
        elif b7['text'] == b5['text'] == b9['text'] != " ":
            print(f"{b7['text']} Wins!")
            game_over(b7['text'])

        elif b3['text'] == b6['text'] == b9['text'] != " ":
            print(f"{b3['text']} Wins!")
            game_over(b3['text'])

        elif b3['text'] == b5['text'] == b7['text'] != " ":
            print(f"{b3['text']} Wins!")
            game_over(b3['text'])

        try:    
            if tries[8] == 1 or tries[8] == 0: game_over(False)
        except: pass
    except:pass

b1 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b1'))
b1.grid(row = 0, column = 0)
b2 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b2'))
b2.grid(row = 0, column = 2)
b3 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b3'))
b3.grid(row = 0, column = 4)
b4 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b4'))
b4.grid(row = 2, column = 0)
b5 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b5'))
b5.grid(row = 2, column = 2)
b6 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b6'))
b6.grid(row = 2, column = 4)
b7 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b7'))
b7.grid(row = 4, column = 0)
b8 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b8'))
b8.grid(row = 4, column = 2)
b9 = Button(rt, text = " ", font = ('segoe ui', 30), padx = 20, command = lambda:main_def('b9'))
b9.grid(row = 4, column = 4)

g1 = Label(rt, text = "|", font = ('segoe ui', 35)).grid(row = 0, column = 1)
g2 = Label(rt, text = "|", font = ('segoe ui', 35)).grid(row = 0, column = 3)
g3 = Label(rt, text = "|", font = ('segoe ui', 35)).grid(row = 2, column = 1)
g4 = Label(rt, text = "|", font = ('segoe ui', 35)).grid(row = 2, column = 3)
g5 = Label(rt, text = "|", font = ('segoe ui', 35)).grid(row = 4, column = 1)
g6 = Label(rt, text = "|", font = ('segoe ui', 35)).grid(row = 4, column = 3)
g7 = Label(rt, text = "---", font = ('segoe ui', 35)).grid(row = 1, column = 0)
g8 = Label(rt, text = "---", font = ('segoe ui', 35)).grid(row = 1, column = 2)
g9 = Label(rt, text = "---", font = ('segoe ui', 35)).grid(row = 1, column = 4)
g10 = Label(rt, text = "---", font = ('segoe ui', 35)).grid(row = 3, column = 0)
g11 = Label(rt, text = "---", font = ('segoe ui', 35)).grid(row = 3, column = 2)
g12 = Label(rt, text = "---", font = ('segoe ui', 35)).grid(row = 3, column = 4)

rt.mainloop()


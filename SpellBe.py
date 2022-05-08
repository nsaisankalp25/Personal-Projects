import tkinter
from tkinter import *
import random, pyttsx3 , time
rt = tkinter.Tk()
file = open(r"C:\Users\Vinod-2018\Desktop\TOTAL SAI THINGS\sai stuff\Sai Programming\Python\pythonVSC\Best Codes real life\reqs\eng_words.txt", 'r')
words_list = file.readlines()
words_list = [go.strip() for go in words_list]
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) 
rate = engine.getProperty('rate')                       
engine.setProperty('rate', 150) 
def spell_def():
    ran_words = random.choice(words_list)
    if ran_words == '':
        spell_def()        
    else:
        print(ran_words)
        for i in range(3):
            engine.say(ran_words)
            engine.runAndWait()
            time.sleep(0.5)

        def sub_def(e):
            spelling = str(spell_e.get())
            if spelling.strip().lower() == ran_words.strip().lower():
                for widgets in rt.winfo_children():
                    widgets.destroy()
                con_statement = "Congrats!, You've got this right"
                cor_l = Label(rt, text = con_statement, font= ("montserrat", 20), fg = 'green')
                cor_l.pack()
                engine.say(con_statement)
                engine.runAndWait()
            else:
                for widgets in rt.winfo_children():
                    widgets.destroy()
                con_statement = """Oops, Better luck next time.
            Anyways, the correct spelling was
            {}""".format(ran_words)    
                cor_l = Label(rt, text = con_statement, font= ("montserrat", 20), fg = 'red')
                cor_l.pack()
                con = con_statement.split(".")
                con = con[0]
                engine.say(con)
                engine.runAndWait()
                
        spell_e = Entry(rt, font = ('segoe ui', 20))
        spell_e.grid(row = 0, column = 1)
        sub_b = Button(rt, text = "Submit", font = ('cambria', 15), command = lambda: sub_def(1))
        sub_b.grid(row = 1, column = 1)
        spell_e.bind("<Return>", sub_def)

def rules_def():
    engine.say("""
    Rules of the competition:
    The system will say out a word 3 times.
    the user is expected to listen to those words carefully and enter the 
    spelling of the word in the text box provided below.
    once entered, click on submit button or just submit by clicking enter.  .
    """)
    engine.runAndWait()

rt.title("Spell Bee - Sai Sankalp")
rt.geometry('600x600')
listen_b = Button(rt, text = "Press to Listen", fg = 'red', font = ('montserrat', 15),
command = spell_def)
listen_b.grid(row = 0, column = 0)
rules_b = Button(rt, text = 'Rules', fg = 'blue', font= ("calibri", 13), command = rules_def)
rules_b.grid(row = 1, column = 0)
rt.mainloop()

print("this is fun!")

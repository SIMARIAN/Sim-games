from tkinter import *
import random

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
score = 0
timeleft = 30 
def startGame(event):
    if timeleft == 30:
        countdown()
    nextColour()
def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score))  
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "+ str(timeleft))
        timeLabel.after(1000, countdown)
        
g = Tk()
g.title("guess the colour")
g.geometry("1150x630+0+0")
g['bg']='#46f3d3'
g.resizable(False,False)
g.iconbitmap(r'icon img ico.ico')
canvas1=Canvas(g,width=10,height=500,bg='grey').place(x=50,y=100)
canvas2=Canvas(g,width=10,height=450,bg='blue').place(x=100,y=100)
canvas3=Canvas(g,width=10,height=400,bg='grey').place(x=150,y=100)
canvas4=Canvas(g,width=10,height=350,bg='blue').place(x=200,y=100)
canvas5=Canvas(g,width=10,height=350,bg='blue').place(x=950,y=100)
canvas6=Canvas(g,width=10,height=400,bg='grey').place(x=1000,y=100)
canvas7=Canvas(g,width=10,height=450,bg='blue').place(x=1050,y=100)
canvas8=Canvas(g,width=10,height=500,bg='grey').place(x=1100,y=100)

instructions = Label(g, text = "Type in the colour of the words,and not the word text!",font = ('arial', 30,'bold'),fg='blue',bg='#46f3d3').pack() 
scoreLabel = Label(g, text = "Press enter to start", font = ('Helvetica', 30),bg='#46f3d3')
scoreLabel.pack()
timeLabel = Label(g, text = "Time left: " + str(timeleft), font = ('Helvetica', 30),bg='#46f3d3')              
timeLabel.pack()
label = Label(g, font = ('Helvetica', 60),bg='#46f3d3')
label.pack()
e = Entry(g,bg="white",font=("arial",30),width=16)
g.bind('<Return>', startGame)
e.place(x=410,y=350)
e.focus_set()
B5=Button(g,bg="black",fg="#46f3d3",text="PREVIOUS PAGE",font=("arial",30,'bold'),command=g.destroy).place(x=410,y=510)
g.mainloop()

import random
import os
from tkinter import*
from PIL import ImageTk, Image

r1=Tk()
r1.bg=ImageTk.PhotoImage(file=r"final picture.jpg")
r1.bg_img=Label(r1,image=r1.bg).place(x=0,y=0)
r1.geometry("1150x630+0+0")
r1.iconbitmap(r'icon img ico.ico')
r1.title("sim-games")
r1.resizable(False,False)

def feedback():
    w = Tk()
    w.geometry("1150x630+0+0")
    w.iconbitmap(r'icon img ico.ico')
    w.title("feedbacks")
    w['bg']='pink'
    w.resizable(False,False)
    canvas1=Canvas(w,width=10,height=500,bg='black').place(x=750,y=100)
    canvas2=Canvas(w,width=10,height=450,bg='black').place(x=710,y=60)
    canvas3=Canvas(w,width=10,height=450,bg='black').place(x=1060,y=60)
    canvas4=Canvas(w,width=10,height=500,bg='black').place(x=1100,y=100)
    def open_txt():
        f = open('feedbacks.txt', 'r')
        s = f.read()
        txtarea.insert(END, s)
        f.close()
    def save_txt():
        f = open('feedbacks.txt', 'w')
        f.write(txtarea.get(1.0, END))
    txtarea= Text(w, width=50, height=20, font=("Helvetica", 18), selectbackground="yellow", selectforeground="black", undo=True)
    txtarea.place(x=10,y=40)
    open_button = Button(w, text="Open Text File",font=("arial",18), bg="orange",fg="black", command=open_txt)
    open_button.place(x=810,y=100)
    save = Button(w, text="Save File",bg="orange",fg="black",font=("arial",18), command=save_txt)
    save.place(x=840,y=200)
    undo = Button(w, text="Undo",bg="lightblue",fg="black",font=("arial",18), command=txtarea.edit_undo)
    undo.place(x=860,y=300)
    redo = Button(w, text="Redo",bg="lightblue",fg="black",font=("arial",18), command=txtarea.edit_redo)
    redo.place(x=860,y=400)
    B5=Button(w,bg="orange",fg="black",text="PREVIOUS PAGE",font=("arial",18),command=w.destroy)
    B5.place(x=800,y=500)
    w.mainloop()

def instructions_gtc():
    r3=Tk()
    r3['bg']='#f52988'
    r3.geometry("1150x630+0+0")
    r3.title("rule1")
    r3.resizable(False,False)
    canvas1=Canvas(r3,width=10,height=550,bg='black').place(x=50,y=20)
    canvas2=Canvas(r3,width=10,height=500,bg='black').place(x=100,y=40)
    canvas3=Canvas(r3,width=10,height=500,bg='black').place(x=1050,y=40)
    canvas4=Canvas(r3,width=10,height=550,bg='black').place(x=1100,y=20)
    txtarea= Text(r3,font=("arial",25), width=50, height=10, selectbackground="yellow", selectforeground="black")
    txtarea.place(x=130,y=30)
    tf = open("rule1.txt")
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
    B5=Button(r3,bg="lightblue",fg="black",text="PREVIOUS PAGE",font=("arial",30),command=r3.destroy)
    B5.place(x=410,y=510)
    r3.mainloop()
def gtc():
    os.system('guess_colour.py')
def guesscolour():
    g1=Tk()
    g1['bg']='#fb0'
    g1.geometry("1150x630+0+0")
    g1.title("guess the colour")
    g1.resizable(False,False)
    title1=Label(g1,text="GUESS THE COLOUR",font=("constantia",35,"bold"),width=20,bg="#fb0", fg="black")
    title1.place(x=260,y=50)
    canvas1=Canvas(g1,width=10,height=550,bg='black').place(x=50,y=20)
    canvas2=Canvas(g1,width=10,height=500,bg='black').place(x=100,y=40)
    canvas3=Canvas(g1,width=10,height=450,bg='black').place(x=150,y=60)
    canvas4=Canvas(g1,width=10,height=400,bg='black').place(x=200,y=80)
    canvas5=Canvas(g1,width=10,height=400,bg='black').place(x=950,y=80)
    canvas6=Canvas(g1,width=10,height=450,bg='black').place(x=1000,y=60)
    canvas7=Canvas(g1,width=10,height=500,bg='black').place(x=1050,y=40)
    canvas8=Canvas(g1,width=10,height=550,bg='black').place(x=1100,y=20)
    Bb1=Button(g1,bg="white",fg="black",text="INSTRUCTIONS",font=("arial",30),width=25,command=instructions_gtc)
    Bb1.place(x=280,y=200)
    Bb2=Button(g1,bg="white",fg="black",text="START THE GAME",font=("arial",30),width=25,command=gtc)
    Bb2.place(x=280,y=300)
    Bb3=Button(g1,bg="white",fg="black",text="FEEDBACKS",font=("arial",30),width=25,command=feedback)
    Bb3.place(x=280,y=400)
    Bb4=Button(g1,bg="lightgreen",fg="black",text="PREVIOUS PAGE",font=("arial",30),command=g1.destroy)
    Bb4.place(x=280,y=510)
    g1.mainloop()

def instructions_rps():
    r3=Tk()
    r3['bg']='#f52988'
    r3.geometry("1150x630+0+0")
    r3.title("INSTRUCTIONS")
    r3.resizable(False,False)
    canvas1=Canvas(r3,width=10,height=550,bg='black').place(x=50,y=20)
    canvas2=Canvas(r3,width=10,height=500,bg='black').place(x=100,y=40)
    canvas3=Canvas(r3,width=10,height=500,bg='black').place(x=1050,y=40)
    canvas4=Canvas(r3,width=10,height=550,bg='black').place(x=1100,y=20)
    txtarea= Text(r3,font=("arial",25), width=50, height=10, selectbackground="yellow", selectforeground="black")
    txtarea.place(x=130,y=30)
    tf = open("rules.txt")
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
    B5=Button(r3,bg="lightblue",fg="black",text="PREVIOUS PAGE",font=("arial",30),command=r3.destroy)
    B5.place(x=410,y=510)
    r3.mainloop()
def rps():
    os.system('rps_code.py')
def rockpaperscissor():
    p2=Tk()
    p2['bg']='#fb0'
    p2.geometry("1150x630+0+0")
    p2.title("rock paper scissor")
    p2.resizable(False,False)
    title1=Label(p2,text="ROCK PAPER SCISSOR",font=("constantia",35,"bold"),width=20,bg="#fb0", fg="black")
    title1.place(x=260,y=50)
    canvas1=Canvas(p2,width=10,height=550,bg='black').place(x=50,y=20)
    canvas2=Canvas(p2,width=10,height=500,bg='black').place(x=100,y=40)
    canvas3=Canvas(p2,width=10,height=450,bg='black').place(x=150,y=60)
    canvas4=Canvas(p2,width=10,height=400,bg='black').place(x=200,y=80)
    canvas5=Canvas(p2,width=10,height=400,bg='black').place(x=950,y=80)
    canvas6=Canvas(p2,width=10,height=450,bg='black').place(x=1000,y=60)
    canvas7=Canvas(p2,width=10,height=500,bg='black').place(x=1050,y=40)
    canvas8=Canvas(p2,width=10,height=550,bg='black').place(x=1100,y=20)
    Bb1=Button(p2,bg="white",fg="black",text="INSTRUCTIONS",font=("arial",30),width=25,command=instructions_rps)
    Bb1.place(x=280,y=200)
    Bb2=Button(p2,bg="white",fg="black",text="START THE GAME",font=("arial",30),width=25,command=rps)
    Bb2.place(x=280,y=300)
    Bb3=Button(p2,bg="white",fg="black",text="FEEDBACKS",font=("arial",30),width=25,command=feedback)
    Bb3.place(x=280,y=400)
    Bb4=Button(p2,bg="lightgreen",fg="black",text="PREVIOUS PAGE",font=("arial",30),command=p2.destroy)
    Bb4.place(x=280,y=510)
    p2.mainloop()

def play():
    r2=Tk()
    r2['bg']='pink'
    r2.geometry("1150x630+0+0")
    r2.iconbitmap(r'icon img ico.ico')
    r2.title("please select the game type")
    r2.resizable(False,False)
    canvas1=Canvas(r2,width=10,height=550,bg='black').place(x=50,y=20)
    canvas2=Canvas(r2,width=10,height=500,bg='black').place(x=100,y=40)
    canvas3=Canvas(r2,width=10,height=450,bg='black').place(x=150,y=60)
    canvas4=Canvas(r2,width=10,height=400,bg='black').place(x=200,y=80)
    canvas5=Canvas(r2,width=10,height=400,bg='black').place(x=950,y=80)
    canvas6=Canvas(r2,width=10,height=450,bg='black').place(x=1000,y=60)
    canvas7=Canvas(r2,width=10,height=500,bg='black').place(x=1050,y=40)
    canvas8=Canvas(r2,width=10,height=550,bg='black').place(x=1100,y=20)
    greeting=Label(r2,text="HELLO "+box.get(),font=("constantia",35,"bold",'underline'),width=20,bg="pink", fg="black").place(x=180,y=50)
    B1=Button(r2,bg="white",fg="black",text="GUESS THE COLOUR",font=("arial",30),width=25,command=guesscolour)
    B1.place(x=280,y=200)
    B2=Button(r2,bg="white",fg="black",text="ROCK PAPER SCISSOR",font=("arial",30),width=25,command=rockpaperscissor)
    B2.place(x=280,y=300)
    B3=Button(r2,bg="lightgreen",fg="black",text="PREVIOUS PAGE",font=("arial",30),command=r2.destroy)
    B3.place(x=280,y=510)
    r2.mainloop()

f1=Frame(r1,bg="pink",width=600,height=200)
f1.place(x=50,y=50)
caption=Label(f1,text="WELCOME TO SIM-GAMES",font=("Constantia",32,"bold","underline"),bg="pink",fg="black")
caption.place(x=20,y=50)
caption99=Label(f1,text="PARADISE OF GAMES",font=("Constantia",20,"underline"),bg="pink",fg="black")
caption99.place(x=150,y=100)
f2=Frame(r1,bg="lightblue",width=450,height=200)
f2.place(x=650,y=400)
ques=Label(f2,text="Player Name = ",font=("arial",20),bg="lightblue",fg="white")
ques.place(x=20,y=50)
box=Entry(f2,bg="white",font=("arial",20),width=15)
box.place(x=210,y=50)
button_play=Button(f2,bg="white",fg="black",text="PLAY",font=("arial",20),command=play)
button_play.place(x=100,y=120)
button_exit=Button(f2,bg="white",fg="black",text="EXIT",font=("arial",20),command=r1.destroy)
button_exit.place(x=300,y=120)
r1.mainloop()
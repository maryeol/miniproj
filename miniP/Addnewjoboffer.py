from tkinter import *

def add():
    f=Tk()
    f.title("Add ")
    f.geometry("250x250")
    f['bg']="#A0A0A0"
    
    a=Label(f,text="Add new job offer:",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    fr=Frame(f,bg="#F8F8FF",borderwidth=5,relief=RAISED)
    fr.pack()
    
    
    
    Label(fr,text="Job ID",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    Label(fr,text="Company information",bg="#F8F8FF").pack(side="left")
    
    
   
    
    Label(fr,text="name",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    Label(fr,text="adresse",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    Label(fr,text="phone number",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    Label(fr,text="email",bg="#F8F8FF").pack()
    user=StringVar()
    a1=Entry(fr,textvariable=user,bg='#FFFAFA')
    a1.pack()
    
    f1=Frame(f,bg="#F8F8FF",borderwidth=5,relief=RAISED,width=400,height=400)
    Label(f1,text="Requested profile description",bg="#F8F8FF").pack()
    
    
    
    
    f.mainloop()
add()    
from tkinter import *
from Addnewjoboffer import add
def admin(adm):
    f=Tk()
    f.title("welcome admin")
    f.geometry("250x250")
    f['bg']="#A0A0A0"
    
    a=Label(f,text="WELCOME MR "+adm+"PLEASE CHOOSE FROM OPTIONS BELOW",fg="black",bg="#A0A0A0")
    a.pack()
    a.config(font=("Courier", 10))
    Label(f,text="OPTIONS",fg="#000000",bg="#A0A0A0",font = "Helvetica 16 bold italic").pack()
    fr=Frame(f,bg="#A0A0A0",borderwidth=2,relief=RAISED, width=400, height=400)
    fr.pack()
    
    
    Button(fr,text="Add new job offer",command=Addnewjoboffer).pack()
    Button(fr,text="Brows and Update a job offer").pack()
    Button(fr,text="Delete a job offer").pack()
    Button(fr,text="Brows the list of job seekers").pack()
    f.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    



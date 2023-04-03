from tkinter import*

root=Tk()
root.title("This is for practice tkinter")
root.configure(background="red")
root.geometry("800x600")
frame=LabelFrame(root,text="My name is Rayhan",padx=10,pady=50)
#frame.pack(padx=0,pady=0)
def close_window():
    root.destroy()
    exit()


def click():
    entered_text=textentry.get()
    output.delete(0.0,END)
    try:definition=my_compdictionary[entered_text]
    except:
        definition="sorry there is no word like that please try again"
        output.insert(END,definition)

Label(root,text="Rayhan",bg="white",fg="black" ).grid(row=0,column=0,)
Label(root,text="Rimi",bg="White",fg="Red" ).grid(row=1,column=1,)
textentry=Entry(root,width=20,bg="white",fg="black",font=('arial',24,'bold'))
textentry.grid(row=2,column=0)
my_compdictionary={
    'algorithm':'step by step instrucctions to complete a task','bug': 'piece of code that causes harm to the computer'
}
Button(root,text="Submit",width=8,command=click).grid(row=2,column=1)
Label(root,text="Definition",bg="black",fg="white",font=('arial',24,'bold') ).grid(row=3,column=1)
output=Text(root,width=75,height=20,wrap=WORD,bg="white")
output.grid(row=5,column=0,columnspan=2)
Label(root,text="Click to Exit",bg="black",fg="white",font=('arial',12,'bold')).grid(row=6,column=1)
Button(root,text=" Exit",bg="White",fg="red",command=close_window,font=('arial',12,'bold')).grid(row=7,column=1)


#Rayhan.pack()


#root.geometry.minsize(200,100)
#root.geometry.maxsize(1000,700)


root.mainloop()
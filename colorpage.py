from tkinter import *
from random import *


def bgg(event):
	a=randint(0,6)
	a2=randint(0,6)
	fr2=Frame().grid()
	colors=("red","orange","blue","indigo","orange","violet","green")
	col=colors[a]
	col2=colors[a2]
	fr=Frame(r,width=300,height=600,bg=col)
	fr.bind('<Button-1>',bgg)
	fr.grid(row=0,column=0)
	Label(fr2,text='HELLO WORLD',font=('arial',24,'bold'),bg=col,fg=col2).grid(row=0,column=0)
r=Tk()
col='red'
fr=Frame(r,width=300,height=600,bg=col)
fr.bind('<Button-1>',bgg)
fr.grid(row=0,column=0)

r.mainloop()

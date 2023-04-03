from tkinter import*
from tkinter import ttk
import time
from tkinter import messagebox
master = Tk()
    


class Main():
  def __init__(self):
    global master
    self.master = master
    self.bg="#8988ef"
    self.bgb="#9a99ff"

    Main.main(self)

  def main(self):
    def ccm():
      self.noCakes.config(state="normal")
      
    def pcm():
      self.noPizza.config(state="normal")
      
    def bcm():
      self.noBurger.config(state="normal")
      
    def scm():
      self.noSandwich.config(state="normal")

    def ncm():
      self.noNuduls.config(state="normal")

    def zcm():
      self.noPancake.config(state="normal")

    def hcm():
      self.noHotdog.config(state="normal")

    def tcm():
      self.noPastri.config(state="normal")

    def iExit():
      iExit = Tk.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
      if iExit > 0:
        root.destroy()
        return

    def calculate():
      cakes = 0
      pizza = 0
      burger = 0
      sandwich = 0
      Nuduls = 0
      Pancake = 0
      Hotdog = 0
      Pastri = 0
      Pcakes = 0
      Ppizza = 0
      Pburger = 0
      Psandwich = 0
      PNuduls = 0
      PPancake = 0
      PHotdog = 0
      PPastri = 0

      if len(self.noCakes.get())>0:
        cakes = int(self.noCakes.get())
        Pcakes = cakes*270
        Label(self.master, text=Pcakes, bg="#a9e", font="arial -13 normal", fg="#023", width=15, height=2,relief=SUNKEN, bd=1).grid(row=2, column=7)

      if len(self.noPizza.get())>0:
        pizza = int(self.noPizza.get())
        Ppizza = pizza*250
        Label(self.master, text=Ppizza, bg="#a9e", font="arial -13 normal", fg="#023", width=15, height=2, relief=SUNKEN, bd=1).grid(row=3, column=7)


      if len(self.noBurger.get())>0:
        burger = int(self.noBurger.get())
        Pburger = burger*85
        Label(self.master, text=Pburger, bg="#a9e", font="arial -13 normal", fg="#023", width=15, height=2, relief=SUNKEN, bd=1).grid(row=4, column=7)


      if len(self.noSandwich.get())>0:
        sandwich = int(self.noSandwich.get())
        Psandwich = sandwich*45
        Label(self.master, text=Psandwich, bg="#a9e", font="arial -13 normal", fg="#023", width=15, height=2, relief=SUNKEN, bd=1).grid(row=5, column=7)

      if len(self.noNuduls.get())>0:
        Nuduls = int(self.noNuduls.get())
        PNuduls = Nuduls*400
        Label(self.master, text=PNuduls, bg="#a9e", font="arial -13 normal", fg="#023", width=15, height=2,relief=SUNKEN, bd=1).grid(row=6, column=7)

      if len(self.noPancake.get())>0:
        Pancake = int(self.noPancake.get())
        PPancake = Pancake*300
        Label(self.master, text=PPancake, bg="#a9e", font="arial -13 normal", fg="#023", width=15, height=2,relief=SUNKEN, bd=1).grid(row=7, column=7)


      if len(self.noHotdog.get())>0:
        Hotdog = int(self.noHotdog.get())
        PHotdog = Hotdog*200
        Label(self.master, text=PHotdog, bg="#a9e", font="arial -13 normal", fg="#023", width=15, height=2,relief=SUNKEN, bd=1).grid(row=8, column=7)


      if len(self.noPastri.get())>0:
        Pastri = int(self.noPastri.get())
        PPastri = Pastri*100
        Label(self.master, text=PPastri, bg="#a9e", font="arial -13 normal", fg="#023", width=15, height=2,relief=SUNKEN, bd=1).grid(row=9, column=7)

      sTotal = Pcakes + Ppizza + Pburger + Psandwich + PPastri +  PHotdog + PPancake +  PNuduls
      tAmmount = (15/100)*sTotal
      discount = (15/100)*sTotal
      total = sTotal + tAmmount - discount

      self.sT.set(str(sTotal))
      self.tA.set(str(tAmmount))
      self.d.set(str(discount))
      self.t.set(str(total))

    def reset():
      self.master.destroy()
      self.master=Tk()
      Main.main(self)
      
    self.master.title("Restaurant")
    self.master.wm_attributes("-topmost", 1)
    self.master.config(bg = self.bg)
    
    Label(self.master, text="", font="arial -15 bold", bg=self.bg, width=20).grid(row=0, column=0)

    Label(self.master, text="Restaurant", font="arial -25 bold", bg=self.bg, fg="pink").grid(row=1, column=7)
    Label(self.master, text="Management", font="arial -25 bold", bg=self.bg, fg="black").grid(row=1, column=8)
    Label(self.master, text="Rayhaner", font="arial -25 bold", bg=self.bg, fg="red").grid(row=1, column=6)
    Label(self.master, text="System", font="arial -25 bold", bg=self.bg, fg="red").grid(row=1, column=9)

    Checkbutton(self.master, text="Cakes     ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2, command=ccm).grid(row=2, column=5)
    Checkbutton(self.master, text="Pizza     ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2, command=pcm).grid(row=3, column=5)
    Checkbutton(self.master, text="Burger    ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2, command=bcm).grid(row=4, column=5)
    Checkbutton(self.master, text="Sandwich  ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2, command=scm).grid(row=5, column=5)

    Checkbutton(self.master, text="Nuduls    ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2, command=ncm).grid(row=6, column=5)
    Checkbutton(self.master, text="Pancake   ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2, command=zcm).grid(row=7, column=5)
    Checkbutton(self.master, text="Hotdog    ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2, command=hcm).grid(row=8, column=5)
    Checkbutton(self.master, text="Pastri    ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2, command=tcm).grid(row=9, column=5)


    self.noCakes = Entry(self.master, width=9, bd=1, state="disabled")
    self.noCakes.grid(row=2, column=6)

    self.noPizza = Entry(self.master, width=9, bd=1, state="disabled")
    self.noPizza.grid(row=3, column=6)

    self.noBurger = Entry(self.master, width=9, bd=1, state="disabled")
    self.noBurger.grid(row=4, column=6)

    self.noSandwich = Entry(self.master, width=9, bd=1, state="disabled")
    self.noSandwich.grid(row=5, column=6)

    self.noNuduls = Entry(self.master, width=9, bd=1, state="disabled")
    self.noNuduls.grid(row=6, column=6)

    self.noPancake = Entry(self.master, width=9, bd=1, state="disabled")
    self.noPancake.grid(row=7, column=6)

    self.noHotdog = Entry(self.master, width=9, bd=1, state="disabled")
    self.noHotdog.grid(row=8, column=6)

    self.noPastri = Entry(self.master, width=9, bd=1, state="disabled")
    self.noPastri.grid(row=9, column=6)

    Button(self.master, text="Reset", font="arial -17 normal", bg=self.bgb, width=15, command=reset).grid(row=11, column=7)
    Button(self.master, text="Calculate", font="arial -17 normal", bg=self.bgb, width=15, command=calculate).grid(row=11, column=8)
    Button(self.master, text="Exit", font="arial -17 normal", bg=self.bgb, width=15, command=master.quit).grid( row=11, column=10)
    Button(self.master, text="Print", font="arial -17 normal", bg=self.bgb, width=15, command=print).grid(row=11, column=9)


    Label(self.master, text="Sub-Total      ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2).grid(row=2, column=9)
    Label(self.master, text="Tax Ammount", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2).grid(row=3, column=9)
    Label(self.master, text="Discount      ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2).grid(row=4, column=9)
    Label(self.master, text="Total            ", bg=self.bg, font="arial -17 normal", fg="#023", width=15, height=2).grid(row=5, column=9)

    self.sT = StringVar()
    self.tA = StringVar()
    self.d = StringVar()
    self.t = StringVar()

    Label(self.master, textvariable=self.sT, bg="#fff", font="arial -13 normal", fg="#023", width=15, height=2, relief=SUNKEN, bd=1).grid(row=2, column=10)
    Label(self.master, textvariable=self.tA, bg="#fff", font="arial -13 normal", fg="#023", width=15, height=2, relief=SUNKEN, bd=1).grid(row=3, column=10)
    Label(self.master, textvariable=self.d, bg="#fff", font="arial -13 normal", fg="#023", width=15, height=2, relief=SUNKEN, bd=1).grid(row=4, column=10)
    Label(self.master, textvariable=self.t, bg="#fff", font="arial -13 normal", fg="#023", width=15, height=2, relief=SUNKEN, bd=1).grid(row=5, column=10)

    Label(self.master, text="", font="arial -15 bold", bg=self.bg, width=20).grid(row=0, column=11)
    Label(self.master, text="", font="arial -15 bold", bg=self.bg, width=20).grid(row=7, column=11)
    Label(self.master, text="", font="arial -15 bold", bg=self.bg, width=20).grid(row=8, column=11)
    

Main()
master.mainloop()

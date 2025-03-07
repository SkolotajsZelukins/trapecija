# s = (a+b)*h/2
from tkinter import *
logs = Tk()
logs.geometry("400x400")
label1 = Label(text="Trapecijas laukuma noteikšana")
label1.pack()
mala1 = Entry()
mala1.pack()
mala2 = Entry()
mala2.pack()
augst = Entry()
augst.pack()
def laukums():
  a = float(mala1.get())
  b = float(mala2.get())
  h = float(augst.get())
  s = (a+b)*h/2
  s.configure(text= s)
  

btn = Button(text="Noteikt laukums",command=laukums)
btn.pack()
label2 = Label(text="")
label2.pack()


logs.mainloop()

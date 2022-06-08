from tkinter import *
  
gui = Tk()

var = StringVar()
msg = Message( gui, textvariable=var, relief=RAISED )

var.set("Hello, Welcome")
msg.pack()
gui.mainloop()

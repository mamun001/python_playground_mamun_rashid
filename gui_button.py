from tkinter import *
root=Tk()
root.title("Mamun Title")
root.geometry("800x800")

mygui = Frame(root)
mygui.grid()

button1 = Button(mygui, text = "Aadeeb")
button1.grid()
button2 = Button(mygui, text = "Aameem")
button2.grid()


root.mainloop()



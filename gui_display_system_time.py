from tkinter import Tk, Label, Button
import datetime

class GUIFUNCTION:
    def __init__(self, master):
        self.master = master
        master.title("Mamun Writes Python")

        self.label = Label(master, text="This is Mamun's GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Click here to write to get system time", command=self.print_time)
        self.greet_button.pack()

        self.close_button = Button(master, text="Click here Close the GUI", command=master.quit)
        self.close_button.pack()


    def print_time(self):
        a=datetime.datetime.now()
        print (a)
        print(datetime.datetime.now())




root = Tk()
my_gui = GUIFUNCTION(root)
root.geometry("400x400")
root.mainloop()

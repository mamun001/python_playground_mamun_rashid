from tkinter import Tk, Label, Button

class GUIFUNCTION:
    def __init__(self, master):
        self.master = master
        master.title("Mamun Writes Python")

        self.label = Label(master, text="This is Mamun's GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Click me to write", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Click me Close the GUI", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Mamun's GUI worked!")

root = Tk()
my_gui = GUIFUNCTION(root)
root.mainloop()

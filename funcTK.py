import tkinter as tk
from tkinter import messagebox
class App:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("I hate IG")
        self.root.geometry("500x500")
        

        self.label = tk.Label(self.root, text = "Fuck IG", fon=("New Times Roman", 12))
        self.label.pack(padx= 10, pady= 10)

        self.textbox = tk.Text(self.root, height=2, background= "gray", cursor= "spider" )
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx = 10, pady = 10 )

        self.checkstate = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text= "Click if you hate IG", height= 2, width=20, background="orange", relief="groove", variable = self.checkstate)
        self.check.pack(padx=10, pady= 10)
        
        self.btn = tk.Button(self.root, text = "Last Last", fg= "purple", command = self.show_mess)
        self.btn.pack(padx = 10, pady = 10)

        self.quit = tk.Button(self.root, text = "QUIT", fg = "red", command=quit)
        self.quit.pack(padx = 10, pady = 10)


        self.root.mainloop()
    def show_mess(self):
        if self.checkstate.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title = "Message", message = self.textbox.get("1.0", tk.END))
    def shortcut(self,event):
        if event.keysym == "Return" and event.state == 8:
            self.show_mess()
        # print("Key sym", event.keysym)
        # print("state", event.state)
app = App()

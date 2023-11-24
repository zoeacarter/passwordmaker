from tkinter import *
from tkinter import messagebox
import string
import secrets

parent_screen = Tk()
parent_screen.geometry("800x800")
#backgroud color = #8A8790
parent_screen.config( bg = "#8A8790")
parent_screen.title("Password Maker")


def hit_button():
    
    msg = messagebox.showinfo("Password", "Your password is ")
pass_btn = Button(parent_screen, text = "Press For Password", command= hit_button,padx="20", pady="20")
pass_btn.place(x = 300, y = 400)
parent_screen.mainloop()

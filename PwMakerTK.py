from tkinter import *
#from tkinter import messagebox
import tkinter as tk
import string
import secrets
class App(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight = 1)
        top.columnconfigure(0, weight= 1)
        self.rowconfigure(0, weight=1)
        self.quit = Button(self, text = "Quit", command= self.quit)
        self.quit.grid(row= 0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        
app = App()
app.master.title("Password Maker")
app.mainloop()






# parent_screen = Tk()
# scr = ttk.Frame(parent_screen, padding=50 )
# #parent_screen.geometry("800x800")
# #backgroud color = #8A8790
# parent_screen.config( bg = "#8A8790")
# parent_screen.title("Password Maker")



# def hit_button():
    
#     msg = messagebox.showinfo("Password", "Your password is ")
# pass_btn = Button(parent_screen, text = "Press For Password", command= hit_button,padx="20", pady="20")
# pass_btn.place(x = 300, y = 400)

# parent_screen.mainloop()
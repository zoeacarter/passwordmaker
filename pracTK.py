import tkinter as tk

#Create the Parent frame
root = tk.Tk()
#Geometry controls how big the main window wil be
root.geometry("400x400")
#Title puts the name of the program in the browswer part of the window
root.title("Test GUI")
root.config(background="black", cursor = "mouse")

#Add a label to the screen - Can be customized like CSS
label = tk.Label(root, text ="Hello World", font =("Times New Roman", 20), background="orange", fg = "Purple")
#Pack(), Grid(), Place() places the widgets on window
label.pack(pady= 50)

#Text puts a text box on the screen
#Good for user inputs/multiple lines of input
textbox = tk.Text(root, height=3, width=5, font =("Times New Roman", 20), background="gray")
textbox.pack()

#Entry creates a textbo with one line max input
#OR when you need a height of 1 textbox
loginentry = tk.Entry(root, background= "red", insertwidth=10, cursor="heart", relief= "groove")
loginentry.pack()



#Mainloop makes the Parent window run
root.mainloop()

# class Tink(tk.Frame):
#     def __init__(self, master = None):
#        tk.Frame.__init__(self, master)
#        self.grid()
     
    
# app = Tink()
# app.master.title("Hello World")
# app.mainloop()
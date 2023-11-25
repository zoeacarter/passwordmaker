'''Basics'''
import tkinter as tk


#Create the Parent frame
root = tk.Tk()
#Geometry controls how big the main window wil be
root.geometry("400x400")
#Title puts the name of the program in the browswer part of the window
root.title("Test GUI")


'''WIDGETS'''

'''Label'''
#Add a label to the screen - Can be customized like CSS
label = tk.Label(root, text ="Hello World", font =("Times New Roman", 20), background="orange", fg = "Purple")
#Pack(), Grid(), Place() places the widgets on window
label.pack(pady= 20)

'''TextBox'''
#Text puts a text box on the screen
#Good for user inputs/multiple lines of input
textbox = tk.Text(root, height=2, width=5, font =("Times New Roman", 20), background="gray")
textbox.pack(pady=30)

'''Entry'''
#Entry creates a textbo with one line max input
#OR when you need a height of 1 textbox
loginentry = tk.Entry(root, background= "red", insertwidth=10, cursor="heart", relief= "groove")
loginentry.pack()

#Grid Layout
#Creates a new frame from root frame
buttonframe = tk.Frame(root)
#Need to configure each column for # of column you want
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

#Use Button Widget
btn1 = tk.Button(buttonframe, text = "1", font = ("New Times Roman", 14))
#Placing button where you want in the grid
#Sticky stretches button east and west so there's not space on the sides
#Can also use tk.N + tk.S for north and south
btn1.grid(row = 0, column = 0, sticky=tk.W+tk.E)

#Repeat for each button
btn2 = tk.Button(buttonframe, text = "2", font = ("New Times Roman", 14))
btn2.grid(row = 0, column = 1, sticky= tk.W+tk.E)

btn3 = tk.Button(buttonframe, text = "3", font = ("New Times Roman", 14))
btn3.grid(row = 0, column = 2, sticky = tk.W+tk.E)

btn4 = tk.Button(buttonframe, text = "4", font = ("New Times Roman", 14))
btn4.grid(row = 1, column = 0, sticky = tk.W+tk.E)

btn5 = tk.Button(buttonframe, text = "5", font = ("New Times Roman", 14))
btn5.grid(row = 1, column = 1, sticky = tk.W+tk.E)

btn6 = tk.Button(buttonframe, text = "6", font = ("New Times Roman", 14))
btn6.grid(row = 1, column = 2, sticky = tk.W+tk.E)

#
buttonframe.pack(pady = 15, fill = "x")

#Place() Funtion - Manually place a widget in the frame
abtn = tk.Button(root, text = "Bish Click")
abtn.place(x=50, y= 100, height= 50, width= 80)

#Button makes buttons
button = tk.Button(root, text = "This is a Button")
button.pack(pady = 20, ipadx=5, ipady=5)




#Made this button to close program easier
qbtn = tk.Button(root, text = "Exit", command= quit)
qbtn.pack(pady = 40, ipadx=5,ipady=5)



#Configures the master (root) Frame
root.config(background="black", cursor = "mouse")
#Mainloop makes the Parent window run
root.mainloop()

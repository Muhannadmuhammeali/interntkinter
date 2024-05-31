import tkinter as tk

root=tk.Tk()


root.geometry("300x300") #set the geometry of the UI


root.title("My first GUI")#title of the UI


label=tk.Label(root,text="UI Basics !",font=('Lexend',18))#heading
label.pack(padx=20,pady=10)#to run everything you can use pack, place and grid


textbox= tk.Text(root,height=1,font=('Arial',11))#to put a text box
textbox.pack()


myentry=tk.Entry(root)#to put a entry
myentry.pack(padx=20,pady=20)


button=tk.Button(root,text="Click me !",font=('Lexend',11))#button creation
button.pack()


buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)


btn1=tk.Button(buttonframe,text="1")
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2=tk.Button(buttonframe,text="2")
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3=tk.Button(buttonframe,text="3")
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4=tk.Button(buttonframe,text="4")
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5=tk.Button(buttonframe,text="5")
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn6=tk.Button(buttonframe,text="6")
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

btn7=tk.Button(buttonframe,text="7")
btn7.grid(row=2,column=0,sticky=tk.W+tk.E)

btn8=tk.Button(buttonframe,text="8")
btn8.grid(row=2,column=1,sticky=tk.W+tk.E)

btn9=tk.Button(buttonframe,text="9")
btn9.grid(row=2,column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill='x')


"""
this is button frame 
sticky is used for ttaching itself to the any side of the button
"""


root.mainloop()# ending of UI

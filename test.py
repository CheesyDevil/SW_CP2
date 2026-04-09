import tkinter as tk 

root=tk.Tk()# main 

root.title("Personal finance")
root.configure(background="") #sets background color
root.minsize(500,500)#sets min size by pixels
root.maxsize(1500,1500) #sets max x and y by pixels
root.geometry("500x500+100+100")#starting x and y and how far it moves


text=tk.Label(root, text="sample text",font=("Times New Roman",30,"bold")) #piece of text
text.grid(row=0,column=0)#adding text to screen

def show_input():
    print("User entered:", text_entry.get())  # Retrieve text with .get()


text_entry=tk.Entry(root,width=75)
text_entry.grid(row=1,column=0,columnspan=2)
submit=tk.Button(root,text="Submit", command=show_input)
submit.grid(row=1,column=2)
option=tk.Button(root,text="option1", command=show_input)
option2=tk.Button(root,text="option1", command=show_input)
option.grid(row=2,column=0,ipadx=75,ipady=50,pady=(10))
option2.grid(row=2,column=1, ipadx=75,ipady=50,pady=(10))
option3=tk.Button(root,text="option1", command=show_input)
option4=tk.Button(root,text="option1", command=show_input)
option3.grid(row=3,column=0,ipadx=75,ipady=50,pady=(10))
option4.grid(row=3,column=1, ipadx=75,ipady=50,pady=(10))
root.mainloop()#keeps it going

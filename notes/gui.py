#SW 2nd Gui Tkinter

import tkinter as tk 

root=tk.Tk()# main 

root.title("Personal")
root.configure(background="green") #sets background color
root.minsize(500,500)#sets min size by pixels
root.maxsize(1500,1500) #sets max x and y by pixels
root.geometry("500x500+100+100")#starting x and y and how far it moves
start=tk.Label(root, text="This is my first GUI",font=("Times New Roman",30,"bold")) #piece of text
start.config(fg="purple", background="green") #sets highlight and tex tcolor
start.grid(row=0,column=0)#adding text to screen

tk.Label(root, text="This is a label").grid(row=1,column=0)# pack makes it appear on screen

#making a counter
root.count=0

def add():
    root.count+=1
    lbl['text']=str(root.count)
def sub():
    root.count-=1
    lbl['text']=str(root.count)

btn=tk.Button(root,text="ADD", command=add)
btn.grid(row=4,column=0,ipadx=5, ipady=5)
btn2=tk.Button(root,text="SUB", command=sub)
btn2.grid(row=4,column=1)

lbl=tk.Label(root, text="0")
lbl.grid(row=5,columnspan=2)

close=tk.Button(root,text="Bye",command=root.destroy)
close.grid(row=6,column=0)
root.mainloop()#keeps it going



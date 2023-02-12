from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("ENDLESS POKEMON CARD GAME")
root.geometry("500x500")
root.configure(background="cyan")

img = ImageTk.PhotoImage(Image.open("button.jpg"))

label_1 = Label(root,text="Player1",bg="White",fg="black",font=('Times',20))
label_1.place(relx=0.9,rely=0.3,anchor=CENTER)

label_2 = Label(root,text="Player2",bg="White",fg="black",font=('Times',20))
label_2.place(relx=0.1,rely=0.3,anchor=CENTER)

label_3 = Label(root,text="",bg="red",fg="white",font=('Times',20))
label_3.place(relx=0.9,rely=0.4,anchor=CENTER)

label_4 = Label(root,text="",bg="red",fg="white",font=('Times',20))
label_4.place(relx=0.1,rely=0.4,anchor=CENTER)

label_5 = Label(root,text="",bg="orange",fg="blue",font=('Times',20))
label_5.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()


from tkinter import *

root = Tk()
root.title('text')
root.geometry('600x400')

frame1 = Frame(root, bg='green')
frame1.pack(side=LEFT)

label1 = Label(frame1, text='label-1')
label1.grid(row=0, column=0)

frame2 = Frame(root)
frame2.pack(side=LEFT)

label2 = Label(frame2, text='label-2')
label2.grid(row=0, column=0)


frame3 = Frame(root)
frame3.pack()

label3 = Label(frame3, text='label-3')
label3.grid(row=0, column=0)


root.mainloop()



# from tkinter import *
#
# def onclick():
#    pass
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
#
# text.tag_add("here", "1.0", "1.4")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="green")
# root.mainloop()
from tkinter import *

class Label_1(Label):
    def __init__(self, master):
        Label.__init__(self, master)
        # self.config(text='Масштаб')

class Entry_1(Entry):
    def __init__(self, master):
        Entry.__init__(self,  master)
        self.insert(0,'enter')

root = Tk()
root.title('Масштаб')
root.geometry('500x400+200+200')

label_scale = Label_1(root)
label_scale.config(justify=RIGHT, text='масштаб', width=5,  bg = 'gray', anchor=W, padx=0, pady=0)
label_scale.place(x=10, y=10, anchor='nw')

# entry_scale1 = Entry_1(root)
# entry_scale1.place(x=50, y = 10)

root.mainloop()
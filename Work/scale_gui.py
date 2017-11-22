from tkinter import *

class Label_1(Label):
    def __init__(self, master):
        Label.__init__(self, master)
        # self.config(text='Масштаб')

class Entry_1(Entry):
    def __init__(self, master):
        Entry.__init__(self,  master)
        self.insert(0,'enter')

class Frame_1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


root = Tk()
root.title('Масштаб')
root.config(bg='gray')
root.geometry('500x400+600+300')

frame_input = Frame_1(root)
frame_input.config(bg='green')
frame_input.place(x = 20, y = 20, width=460, height=30)


label_scale1 = Label_1(frame_input)
label_scale1.config(justify=RIGHT, text='масштаб', width=5,  bg = 'red', anchor=W, padx=0, pady=0)
# label_scale1.grid(, y=10, anchor='nw')

entry_scale1 = Entry_1(frame_input)
entry_scale1.place(x=50, y = 10)

root.mainloop()
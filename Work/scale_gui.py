from tkinter import *

class Label_1(Label):
    def __init__(self, master):
        Label.__init__(self, master)
        self.config(text='Масштаб')

class Entry_1(Entry):
    def __init__(self, master):
        Entry.__init__(self,  master)
        self.insert(0,'enter')
        
class Frame_1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background='green')
        

class Frame_1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)


root = Tk()
root.title('Масштаб')

root.geometry('500x400+200+200')
root.tk_setPalette(background='purple')

frame_input = Frame_1(root)
frame_input['background']='red'
frame_input.place(width=450, anchor='nw', height=30, x=20, y=20)

label_scale = Label_1(frame_input)
label_scale.config(justify=RIGHT, text='масштабsssss', height=2,  bg = 'gray', padx=0, pady=0)
label_scale.grid(row=10, column=10, padx=5)

entry_scale1 = Entry_1(frame_input)
entry_scale1.configure(bg='green', width=10, font='Arial 10')
entry_scale1.grid(row=10, column = 13, sticky='n')


root.mainloop()
from tkinter import *

class Label_1(Label):
    def __init__(self, master):
        Label.__init__(self, master)
        self.config(bg='#ffeaf4')

class Entry_1(Entry):
    def __init__(self, master):
        Entry.__init__(self,  master)
        self.config(bg='#b9b9dd')

class Frame_1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        

class Frame_1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

class Text_1(Text):
    def __init__(self, master):
        Text.__init__(self, master)
        self.config(bg='green')


class Button_1(Button):
    def __init__(self, master):
        Button.__init__(self, master)
        self.configure(bg='purple')

root = Tk()
root.title('Масштаб')
root.geometry('+600+300')
root.tk_setPalette(background='#55ffaa')

frame_root = Frame_1(root)
frame_root.grid(row=0, column=0, padx=20, pady=20)

frame_input = Frame_1(frame_root)
frame_input.grid(row=10, column=10, sticky=W)

label_in_scale=Label_1(frame_input)
label_in_scale.config(text="Масштаб")
label_in_scale.grid(row=10, column=10)

label_razd0 = Label_1(frame_input)
label_razd0.grid(row=10, column=15, padx=5)

entry_scale1 = Entry_1(frame_input)
entry_scale1.config(width=6, justify='c')
entry_scale1.insert(0,1)
entry_scale1.grid(row=10, column=20)

label_razd1 = Label_1(frame_input)
label_razd1.configure(text=':')
label_razd1.grid(row=10, column=25)

entry_scale2 = Entry_1(frame_input)
entry_scale2.config(width=8, justify=CENTER)
entry_scale2.grid(row=10, column=30)


#Вывод
frame_output = Frame_1(frame_root)
frame_output.configure(pady=20)
frame_output.grid(row=20, column=10, sticky=W)

text_out_00 = Label_1(frame_output)
text_out_00.configure(height=1, width=7, text='в 1 мм')
text_out_00.grid(row=10, column=10, sticky=W)

text_out_01 = Label_1(frame_output)
text_out_01.grid(row=10, column=20)

text_out_02 = Label_1(frame_output)
text_out_02.configure(text='м')
text_out_02.grid(row=10, column=30)


text_out_10 = Label_1(frame_output)
text_out_10.configure(height=1, width=7, text='в 1 м')
text_out_10.grid(row=20, column=10, sticky=W)

text_out_11 = Label_1(frame_output)
text_out_11.grid(row=20, column=20)

text_out_12 = Label_1(frame_output)
text_out_12.configure(text='мм')
text_out_12.grid(row=20, column=30)


#кнопки
frame_button = Frame_1(frame_root)
frame_button.grid(row=30, column=10)

button_do = Button_1(frame_button)
button_do.configure(text='Рассчитать')
button_do.grid(row=10, column=10)

root.mainloop()
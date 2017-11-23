from tkinter import *
from tkinter import colorchooser
import time


def func_exit():
    pass

def not_change_hex(event):
    # entry_hex.icursor(0)
    # entry_hex.delete(0, END)
    hex_var.set(value=k[1])
    entry_hex.icursor(0)
    entry_hex.select_from(0)
    entry_hex.select_to(END)


def not_change_dec(event):
    # entry_dec.icursor(0)
    # entry_dec.delete(0, END)
    dec_var.set(value='(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')')
    entry_dec.icursor(0)
    entry_dec.select_from(0)
    entry_dec.select_to(END)


def change(event):
    # time.sleep(0.01)
    hex_var.set(value='0000000000')
    entry_hex.icursor(0)
    entry_hex.select_from(0)
    entry_hex.select_to(END)



root=Tk()
root.title('Номер цвета')
root.geometry('300x200+600+300')
root.config(bg='#369d0b')
root.resizable(width=False, height=False)
# root.protocol('WM_DELETE_WINDOW', func=func_exit)

frame_info = Frame(root, bg='gray')
frame_info.place(x=20, y=20, width=260)

text_dec = Label(frame_info)
text_dec.config(text='none')
text_dec.grid(row = 10, column= 10, padx=3)

text_hex = Label(frame_info)
text_hex.config(text='none')
text_hex.grid(row=10, column=15)


frame_ent = Frame(root, bg='purple')
frame_ent.place(x=20, y=70, width=260)

dec_var = StringVar()
dec_var.set(value='11111')
hex_var = StringVar()
hex_var.set(value='00000')

entry_dec = Entry(frame_ent, textvariable=dec_var)
entry_dec.grid(row = 10, column= 10, padx=3)

entry_hex = Entry(frame_ent, textvariable=hex_var)
entry_hex.grid(row=10, column=15)

root1=Tk()
root1.geometry('+500+300')
root1.overrideredirect(1)
k = colorchooser.askcolor(parent=root1)
root1.destroy()


text_dec['text']='(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')'
text_hex['text']=k[1]

dec_var.set(value='(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')')
hex_var.set(value=k[1])


entry_hex.focus_set()
entry_hex.select_to(END)

entry_hex.bind("<KeyPress>", not_change_hex)
entry_hex.bind("<KeyRelease>", not_change_hex)
entry_hex.bind("<ButtonRelease-3>", change)
# entry_hex.bind("<Button-1-KeyPress>", not_change)

entry_dec.bind("<KeyPress>", not_change_dec)
entry_dec.bind("<KeyRelease>", not_change_dec)
entry_dec.bind("<ButtonRelease>", not_change_dec)


root.mainloop()
print(k[0])
print(k[1])
print(round(160.6))

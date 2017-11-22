from tkinter import *
from tkinter import colorchooser

# print(colorchooser.winfo_id())
# print(k)
# print(k[1])

def func_exit():
    pass


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

hex_var = StringVar()

entry_dec = Entry(frame_ent)
entry_dec.insert(0,'nonenoe')
entry_dec.grid(row = 10, column= 10, padx=3)

entry_hex = Entry(frame_ent, textvariable=hex_var)
entry_hex.insert(0,'nonenone')
entry_hex.grid(row=10, column=15)

root1=Tk()
root1.geometry('+500+300')
k = colorchooser.askcolor(parent=root1,color='#000000')
root1.destroy()

# root.focus_get()

text_dec['text']='(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')'
text_hex['text']=k[1]

entry_dec.delete(0,END)
entry_hex.delete(0,END)

entry_dec.insert(0,'(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')')
entry_hex.insert(0,k[1])

# root.grab_set()

# text_dec = Label(frame_info)
# text_dec.config(text='(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')')
# text_dec.grid(row = 10, column= 10, padx=3)

# text_hex = Label(frame_info)
# text_hex.config(text=k[1])
# text_hex.grid(row=10, column=15)

# frame_ent = Frame(root, bg='purple')
# frame_ent.place(x=20, y=70, width=260)
#
# hex_var = StringVar()
#
#
# entry_dec = Entry(frame_ent)
# entry_dec.grid(row = 10, column= 10, padx=3)
#
# entry_hex = Entry(root, textvariable=hex_var)
# entry_hex.insert(0,k[1])
# entry_hex.grid(row=10, column=15)

root.mainloop()
print(k[0])
print(k[1])
print(round(160.6))
from tkinter import *
from tkinter import colorchooser

# print(colorchooser.winfo_id())
# print(k)
# print(k[1])

root=Tk()
root.title('Номер цвета')
root.geometry('300x200+600+300')
root.config(bg='#369d0b')
root.resizable(width=False, height=False)

k = colorchooser.askcolor(parent=root)

frame_info = Frame(root, bg='gray')
frame_info.place(x=20, y=20, width=260)

text_dec = Label(frame_info)
text_dec.config(text='(' + str(int(k[0][0])) + ',' + str(int(k[0][1])) +',' + str(int(k[0][2])) +')')
text_dec.grid(row = 10, column= 10, padx=3)

text_hex = Label(frame_info)
text_hex.config(text=k[1])
text_hex.grid(row=10, column=15)

frame_ent = Frame(root, bg='purple')
frame_ent.place(x=20, y=70, width=260)

entry_dec = Entry(frame_ent)
entry_dec.grid(row = 10, column= 10, padx=3)

entry_hex = Entry(frame_ent)
entry_hex.grid(row=10, column=15)

root.mainloop()
print(k[0])
print(k[1])
print(round(160.6))
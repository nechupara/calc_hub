from tkinter import *

main = Tk()


def add_button(event):

    position_in_list = button_list.index(event.widget)+1

    button_list.insert(position_in_list,Button(main,text='Добавить...'))
    button_list[position_in_list].bind('<ButtonRelease>',add_button)

    button_del.insert(position_in_list,Button(main,text='Удалить...'))
    button_del[position_in_list].bind('<ButtonRelease>',del_button)

    add_obj(position_in_list)
    draw()

def del_button(event):
    position_in_list = button_del.index(event.widget)

    del button_list[position_in_list]
    del button_del[position_in_list]
    del obj_list[position_in_list]

    button_list[position_in_list].destroy()
    button_del[position_in_list].destroy()
    obj_list[position_in_list].destroy()

    draw()


def draw():
    for i in range(len(button_list)):
        button_list[i].grid(row=i,column=1)
        button_del[i].grid(row=i,column=2)
        obj_list[i].grid(row=i,column=0)


def add_obj(position_in_list):
    obj_list.insert(position_in_list,Label(main,text='....'+\
                    str(position_in_list)+'....'))


button_list = [Button(main,text='Добавить...')]
button_list[0].bind('<ButtonRelease>',add_button)
button_list[0].grid(row=0,column=1)

button_del = [Button(main,text='Удалить...')]
button_del[0].bind('<ButtonRelease>',del_button)
button_del[0].grid(row=0,column=2)

obj_list = [Label(main,text='я тут местный...')]
obj_list[0].grid(row=0,column=0)

main.mainloop()
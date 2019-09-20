from tkinter import *
import backend


def view_cmd():
    box.delete(0, END)
    for row in backend.view():
        box.insert(END, row)


def insert_cmd():
    backend.insert(text_Tit.get(), text_Company.get(), text_Type.get(), text_year.get())
    box.delete(0, END)
    box.insert(END, (text_Tit.get(), text_Company.get(), text_Type.get(), text_year.get()))


def search_cmd():
    box.delete(0, END)
    for row in backend.search(text_Tit.get(), text_Company.get(), text_Type.get(), text_year.get()):
        box.insert(END, row)


def get_selected_row(event):
    global selected_tuple
    index = box.curselection()
    if len(index) != 0:
        selected_tuple = box.get(index[0])
        tup_len = len(selected_tuple)
        print(selected_tuple)
        eTit.delete(0, END)
        eAth.delete(0, END)
        eYr.delete(0, END)
        eType.delete(0, END)

        eTit.insert(END, selected_tuple[tup_len - 4])
        eAth.insert(END, selected_tuple[tup_len - 3])
        eType.insert(END, selected_tuple[tup_len - 2])
        eYr.insert(END, selected_tuple[tup_len - 1])


def update_cmd():
    backend.update(selected_tuple[0], text_Tit.get(), text_Company.get(), text_Type.get(), text_year.get())
    box.delete(0, END)
    view_cmd()


def delete_cmd():
    backend.delete(selected_tuple[0])
    view_cmd()


def close_cmd():
    window.destroy()


# MAIN WINDOW
window = Tk()
window.resizable(0, 0)
window.title("Game Store data base")

# LABELS
lb1 = Label(window, text="Tittle")
lb1.grid(row=0, column=0)
lb2 = Label(window, text="Company")
lb2.grid(row=0, column=2)
lb3 = Label(window, text="Type")
lb3.grid(row=1, column=0)
lb4 = Label(window, text="Year")
lb4.grid(row=1, column=2)

# ENTRY FIELDS
text_Tit = StringVar()
eTit = Entry(window, textvariable=text_Tit)
eTit.grid(row=0, column=1)

text_Company = StringVar()
eAth = Entry(window, textvariable=text_Company)
eAth.grid(row=0, column=3)

text_Type = StringVar()
eType = Entry(window, textvariable=text_Type)
eType.grid(row=1, column=1)

text_year = StringVar()
eYr = Entry(window, textvariable=text_year)
eYr.grid(row=1, column=3)

# BUTTONS

b_vall = Button(window, text="View All", width=12, command=view_cmd)
b_vall.grid(row=2, column=3)

b_sentr = Button(window, text="Search Entry", width=12, command=search_cmd)
b_sentr.grid(row=3, column=3)

b_addentr = Button(window, text="Add Entry", width=12, command=insert_cmd)
b_addentr.grid(row=4, column=3)

b_upselec = Button(window, text="Update Selected", width=12, command=update_cmd)
b_upselec.grid(row=5, column=3)

b_delselec = Button(window, text="Delete Selected", width=12, command=delete_cmd)
b_delselec.grid(row=6, column=3)

b_close = Button(window, text="Close", width=12, command=close_cmd)
b_close.grid(row=7, column=3)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

box = Listbox(window, height=8, width=45)
box.grid(row=2, column=0, rowspan=6, columnspan=2)

box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=box.yview, bg="lightblue", activebackground='blue')

box.bind('<<ListboxSelect>>', get_selected_row)


window.mainloop()

from tkinter import *
from tkinter import messagebox

# Exit protocol
def exit():
    if messagebox.askokcancel("Exit", "Wanna leave?"):
        if messagebox.askokcancel("Exit", "Are you sure?"):
            if messagebox.askokcancel("Exit", "Really?"):
                root.destroy()


# creating root window
root = Tk()

root.protocol("WM_DELETE_WINDOW", exit)

# creating scrollbar for listbox
scrollbarV = Scrollbar(root)
scrollbarH = Scrollbar(root, orient=HORIZONTAL)
scrollbarV.grid(row=3, column=0, rowspan=7, sticky=N+S+E)
scrollbarH.grid(row=10, column=0, rowspan=7, sticky=N+E+S+W)


# changing root window background color
root.configure(bg="snow2")


# Changing the title Title
root.title("My To-Do-List App")


# Change window size
root.minsize("275","275")
root.maxsize("275","275")


#Creating an Empty List
tasks = []


# creating functions
def update_listbox():
    #Clear the current list
    clear_listbox()
    #Populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)


def clear_listbox():
    lb_tasks.delete(0,"end")


def add_task():
    task =txt_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "You need to Enter a task")
    txt_input.delete(0, "end")

def del_all():
    confirmed = messagebox.askyesno("Please Confirm", "Do You Really Want to Delete all tasks")
    if confirmed is True:
        global tasks
        #Clear the task list
        tasks = []
        #update the listbox
        update_listbox()


def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()


def sort_asc():
    tasks.sort()
    update_listbox()


def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()


def show_tasks():
    show_tasks = len(tasks)
    out = "Number of Tasks: %s" %show_tasks
    lbl_display["text"]=out

# creating GUI
lbl_title = Label(root, text="TO-DO-LIST", font ="Verdana 10 underline", fg="#000033", bg='snow2', )
lbl_title.grid(row=0,column=1)

lbl_display = Label(root, text="Please Enter Your Task below", bg='snow2')
lbl_display.grid(row=1,column=0)

txt_input = Entry(root, width=25)
txt_input.grid(row=2,column=0)

btn_add_task = Button(root, text="Add Task", fg="#000033", bg="white", command=add_task, borderwidth=3, width=15)
btn_add_task.grid(row=2,column=1)

btn_del_all = Button(root, text="Delete All", fg="#000033", bg="white", command=del_all, borderwidth=3, width=15)
btn_del_all.grid(row=3,column=1)

btn_del_one = Button(root, text="Delete one", fg="#000033", bg="white", command=del_one, borderwidth=3, width=15)
btn_del_one.grid(row=4,column=1)

btn_sort_asc = Button(root, text="Sort in (ASC)", fg="#000033", bg="white", command=sort_asc, borderwidth=3, width=15)
btn_sort_asc.grid(row=5,column=1)

btn_sort_desc = Button(root, text="Sort in (DESC)", fg="#000033", bg="white", command=sort_desc, borderwidth=3, width=15)
btn_sort_desc.grid(row=6,column=1)

btn_show_tasks = Button(root, text="Number of Tasks", fg="#000033", bg="white", command=show_tasks, borderwidth=3, width=15)
btn_show_tasks.grid(row=7,column=1)

btn_exit = Button(root, text="Exit", fg="#000033", bg="white", command=exit, borderwidth=3, width=15)
btn_exit.grid(row=8,column=1)

lb_tasks = Listbox(root)
lb_tasks.grid(row=3,column=0, rowspan=7)

# attach listbox to scrollbar
lb_tasks.config(yscrollcommand=scrollbarV.set)
scrollbarV.config(command=lb_tasks.yview)

lb_tasks.config(xscrollcommand=scrollbarH.set)
scrollbarH.config(command=lb_tasks.xview)

# Start Mainloop
root.mainloop()
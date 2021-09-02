import tkinter
import tkinter.messagebox
import pickle
root = tkinter.Tk()
root.title("Weekly Grocery List")

def add_task():
    task = entry_task.get()
    if task != "":
        tasks_listbox.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning", message="You must enter a task!")

def delete_task():
    try: #tries this code
        task_index = tasks_listbox.curselection()[0] 
        tasks_listbox.delete(task_index)
    except: #if an error appears, it does this
        tkinter.messagebox.showwarning(title="Warning", message="You must select a task!")


def load_task():
    tasks = pickle.load(open("task.data", "rb"))
    tasks_listbox.delete(0, tkinter.END)
    for task in tasks:
        tasks_listbox.insert(tkinter.END, task)

def save_task():
    tasks = tasks_listbox.get(0, tasks_listbox.size()) #gets all task in list box
    pickle.dump(tasks, open("task.data", "wb"))

#create GUI

framed_task = tkinter.Frame(root)
framed_task.pack()

tasks_listbox = tkinter.Listbox(framed_task, height=10, width=50)
tasks_listbox.pack(side = tkinter.LEFT)
#scroll bar
scroll_bar = tkinter.Scrollbar(framed_task)
scroll_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
tasks_listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command = tasks_listbox.yview)
# task entry
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()
#button to add task
add_task_button = tkinter.Button(root, text = "Add Task", width=48, command=add_task)
add_task_button.pack()

delete_task_button = tkinter.Button(root, text = "Delete Task", width=48, command=delete_task)
delete_task_button.pack()

load_task_button = tkinter.Button(root, text = "Load Tasks", width=48, command=load_task)
load_task_button.pack()

save_task_button = tkinter.Button(root, text = "Save Tasks", width=48, command=save_task)
save_task_button.pack()





root.mainloop()
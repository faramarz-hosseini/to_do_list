import tkinter
import tkinter.messagebox
import pickle
from tkinter import colorchooser


root = tkinter.Tk()
root.title('To Do List BY a_walking_dead')
# color_code = colorchooser.askcolor(title="button colors")[1]
# print(color_code)

class Task:
    @staticmethod
    def get_task():
        return Initializer.entry_task.get()

    @staticmethod
    def select_task():
        return Initializer.listbox_tasks.curselection()

    @staticmethod
    def add_task():
        task = Task.get_task()
        if task != "":
            Initializer.listbox_tasks.insert(tkinter.END, task)
            Initializer.entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="WARNING", message="Please enter a task.")

    @staticmethod
    def edit_task():
        old_task = Task.select_task()
        new_task = Task.get_task()
        if new_task != "":
            try:
                selection_value = Initializer.listbox_tasks.get(Initializer.listbox_tasks.curselection())
                lst = list(Initializer.listbox_tasks.get(0, "end"))
                selection_index = lst.index(selection_value)
                Initializer.listbox_tasks.delete(old_task)
                Initializer.listbox_tasks.insert(selection_index, new_task)
                Initializer.entry_task.delete(0, tkinter.END)
            except:
                tkinter.messagebox.showwarning(title="CAUTION", message="Please select the task you wish to edit first.")
        else:
            tkinter.messagebox.showwarning(title="CAUTION", message="Please type in the new task.")

    @staticmethod
    def del_task():
        task = Task.select_task()
        try:
            Initializer.listbox_tasks.delete(task)
        except:
            tkinter.messagebox.showwarning(title="WARNING", message="Please select a task.")

    @staticmethod
    def save_tasks():
        tasks = Initializer.listbox_tasks.get(0, Initializer.listbox_tasks.size())
        pickle.dump(tasks, open("tasks.dat", "wb"))
        tkinter.messagebox.showinfo(title="STATUS", message="Tasks saved.")

    @staticmethod
    def clear_tasks():
        Initializer.listbox_tasks.delete(0, "end")

    @staticmethod
    def load_tasks():
        try:
            successful_load = False
            tasks = pickle.load(open("tasks.dat", "rb"))
            previous_tasks = Initializer.listbox_tasks.get(0, Initializer.listbox_tasks.size())
            for task in tasks:
                if task in previous_tasks:
                    tkinter.messagebox.showwarning(title="WARNING", message="File already loaded.")
                    return None
                else:
                    successful_load = True
                    Initializer.listbox_tasks.insert(tkinter.END, task)
            if successful_load:
                tkinter.messagebox.showinfo(title="STATUS", message="Tasks successfully loaded.")
        except:
            tkinter.messagebox.showerror(title="ERROR!", message="No tasks to load.")


# GUI
class Gui:
    def __init__(self, listbox_tasks_height=30, listbox_tasks_width=100):
        self.listbox_tasks_height = listbox_tasks_height
        self.listbox_tasks_width = listbox_tasks_width
        # Assets
        self.frame = tkinter.Frame(root)
        self.listbox_tasks = tkinter.Listbox(self.frame, fg="green", bg="black", height=self.listbox_tasks_height, width=self.listbox_tasks_width)
        self.entry_task = tkinter.Entry(root, fg="green", bg="black", width=self.listbox_tasks_width)
        self.menu = tkinter.Menu(root)
        self.filemenu = tkinter.Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="New", command=self.donothing())
        # Assets > Scroll Bar
        self.scrollbar = tkinter.Scrollbar(self.frame)
        self.listbox_tasks.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox_tasks.yview)
        # Assets > Buttons
        self.button_add_task = tkinter.Button(root, text='+Task', bg="green", width=self.listbox_tasks_width,
                                              command=Task.add_task)
        self.button_edit_task = tkinter.Button(root, text='Edit task', bg="green", width=self.listbox_tasks_width,
                                               command=Task.edit_task)
        self.button_del_task = tkinter.Button(root, text='-Task', bg="green", width=self.listbox_tasks_width,
                                              command=Task.del_task)
        self.button_clear_tasks = tkinter.Button(root, text='Clear all tasks', bg="green", width=self.listbox_tasks_width,
                                                 command=Task.clear_tasks)
        self.button_save_tasks = tkinter.Button(root, text='Save Tasks', bg="green", width=self.listbox_tasks_width,
                                                command=Task.save_tasks)
        self.button_load_tasks = tkinter.Button(root, text='Load Tasks', bg="green", width=self.listbox_tasks_width,
                                                command=Task.load_tasks)
        self.button_load_tasks = tkinter.Button(root, text='Load Tasks', bg="green", width=self.listbox_tasks_width,
                                                command=Task.load_tasks)

    def donothing(self):
        pass

    def costumize_buttons(self):
        pass

    def button_loader(self):
        self.button_add_task.pack()
        self.button_edit_task.pack()
        self.button_del_task.pack()
        self.button_clear_tasks.pack()
        self.button_save_tasks.pack()
        self.button_load_tasks.pack()

    def loader(self):
        self.frame.pack()
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.listbox_tasks.pack()
        self.entry_task.pack()
        self.button_loader()


Initializer = Gui()
Initializer.loader()
root.config(menu=Initializer.menu)
root.mainloop()



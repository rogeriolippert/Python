from tkinter import *
from tkinter import ttk

class TodoList:
    def __init__(self, master):
        self.master = master
        self.todo = []
        self.done = []
        self.listbox_todo = Listbox(master)
        self.listbox_done = Listbox(master)
        self.progress = ttk.Progressbar(master, length=200)

    def add_task(self, task):
        self.todo.append(task)
        self.update_ui()

    def complete_task(self, event):
        task = self.listbox_todo.get(ACTIVE)
        if task:
            self.todo.remove(task)
            self.done.append(task)
            self.update_ui()

    def update_ui(self):
        self.listbox_todo.delete(0, END)
        for task in self.todo:
            self.listbox_todo.insert(END, task)

        self.listbox_done.delete(0, END)
        for task in self.done:
            self.listbox_done.insert(END, task)

        total_tasks = len(self.todo) + len(self.done)
        done_tasks = len(self.done)
        if total_tasks:
            self.progress['value'] = (done_tasks / total_tasks) * 100
        else:
            self.progress['value'] = 0

        self.progress.update()

root = Tk()
todo_list = TodoList(root)
todo_list.listbox_todo.bind('<Double-1>', todo_list.complete_task)
todo_list.listbox_todo.pack()
todo_list.listbox_done.pack()
todo_list.progress.pack()
todo_list.add_task("Tarefa 1")
todo_list.add_task("Tarefa 2")

root.mainloop()
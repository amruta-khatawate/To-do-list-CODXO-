import tkinter as tk
from tkinter import filedialog

# Main class for the To-Do List application
class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window size and title
        self.geometry("400x400")
        self.title("To do list")

        # Create and arrange the widgets in the window
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for inputting new tasks
        self.task_input = tk.Entry(self, width=30)
        self.task_input.pack(pady=10)

        # Button to add new tasks to the list
        self.add_task_button = tk.Button(self, text="Add task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Listbox to display the list of tasks
        self.task_listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=5)

        # Frame to hold the edit and delete buttons
        self.buttom_frame = tk.Frame(self)
        self.buttom_frame.pack(pady=5)

        # Button to edit the selected task
        self.edit_task_button = tk.Button(self.buttom_frame, text="Edit Text", command=self.edit_task)
        self.edit_task_button.grid(row=0, column=0, padx=5)

        # Button to delete the selected task
        self.delete_task_button = tk.Button(self.buttom_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=5)

        # Button to save the list of tasks to a file
        self.save_button = tk.Button(self, text="Save", command=self.save_tasks)
        self.save_button.pack(pady=5)

        # Button to load the list of tasks from a file
        self.load_button = tk.Button(self, text="Load", command=self.load_tasks)
        self.load_button.pack(pady=5)

    def add_task(self):
        # Get the task from the input field
        task = self.task_input.get()
        # If the input is not empty, add the task to the listbox and clear the input field
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)

    def edit_task(self):
        # Get the index of the selected task
        task_index = self.task_listbox.curselection()
        # Ensure a task is selected
        if task_index:
            # Get the new task description from the input field
            new_task = self.task_input.get()
            # If the input is not empty, replace the selected task with the new task
            if new_task:
                self.task_listbox.delete(task_index)
                self.task_listbox.insert(task_index, new_task)
                self.task_input.delete(0, tk.END)

    def delete_task(self):
        # Get the index of the selected task
        task_index = self.task_listbox.curselection()
        # If a task is selected, delete it from the listbox
        if task_index:
            self.task_listbox.delete(task_index)

    def save_tasks(self):
        # Get all tasks from the listbox
        tasks = self.task_listbox.get(0, tk.END)
        # Open a save dialog to choose the file path
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        # If a file path is selected, save the tasks to the file
        if file_path:
            with open(file_path, 'w') as file:
                for task in tasks:
                    file.write(task + "\n")

    def load_tasks(self):
        # Open a file dialog to choose the file path
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        # If a file path is selected, load the tasks from the file
        if file_path:
            with open(file_path, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]
            
            # Clear the existing tasks in the listbox
            self.task_listbox.delete(0, tk.END)
            
            # Insert the loaded tasks into the listbox
            for task in tasks:
                self.task_listbox.insert(tk.END, task)

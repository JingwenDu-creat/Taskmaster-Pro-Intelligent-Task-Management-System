import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime

# Initialize database
def initialize_db():
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()

    # Course management
    c.execute('''CREATE TABLE IF NOT EXISTS courses (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 course_name TEXT,
                 schedule TEXT
                 )''')

    # Assignments tracking
    c.execute('''CREATE TABLE IF NOT EXISTS assignments (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 course_id INTEGER,
                 assignment_name TEXT,
                 due_date TEXT,
                 grading_criteria TEXT
                 )''')

    # To-do list
    c.execute('''CREATE TABLE IF NOT EXISTS todos (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 task_name TEXT,
                 category TEXT,
                 priority INTEGER,
                 due_date TEXT
                 )''')

    # Habits tracking
    c.execute('''CREATE TABLE IF NOT EXISTS habits (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 habit_name TEXT,
                 start_date TEXT,
                 frequency INTEGER
                 )''')

    # Personal activities
    c.execute('''CREATE TABLE IF NOT EXISTS activities (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 activity_name TEXT,
                 event_date TEXT
                 )''')

    conn.commit()
    conn.close()

# Add course
def add_course(course_name, schedule):
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("INSERT INTO courses (course_name, schedule) VALUES (?, ?)", (course_name, schedule))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Course added successfully!")

# Add assignment
def add_assignment(course_id, assignment_name, due_date, grading_criteria):
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("INSERT INTO assignments (course_id, assignment_name, due_date, grading_criteria) VALUES (?, ?, ?, ?)",
              (course_id, assignment_name, due_date, grading_criteria))
    conn.commit()
    conn.close()

# Add task to To-do list
def add_todo(task_name, category, priority, due_date):
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos (task_name, category, priority, due_date) VALUES (?, ?, ?, ?)",
              (task_name, category, priority, due_date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Task added successfully!")

# Add habit
def add_habit(habit_name, start_date, frequency):
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("INSERT INTO habits (habit_name, start_date, frequency) VALUES (?, ?, ?)",
              (habit_name, start_date, frequency))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Habit added successfully!")

# Add activity
def add_activity(activity_name, event_date):
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("INSERT INTO activities (activity_name, event_date) VALUES (?, ?)", (activity_name, event_date))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Activity added successfully!")

# Fetch all courses
def get_courses():
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("SELECT * FROM courses")
    courses = c.fetchall()
    conn.close()
    return courses

# Fetch all assignments
def get_assignments():
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assignments")
    assignments = c.fetchall()
    conn.close()
    return assignments

# Fetch all tasks
def get_todos():
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    todos = c.fetchall()
    conn.close()
    return todos

# Fetch all habits
def get_habits():
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("SELECT * FROM habits")
    habits = c.fetchall()
    conn.close()
    return habits

# Fetch all activities
def get_activities():
    conn = sqlite3.connect('taskmaster.db')
    c = conn.cursor()
    c.execute("SELECT * FROM activities")
    activities = c.fetchall()
    conn.close()
    return activities

# GUI Layout
class TaskMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskMaster")
        self.root.geometry("600x400")
        self.root.configure(bg="#f2f2f2")  # Set background color

        # Menu
        menu = Menu(root)
        root.config(menu=menu)

        course_menu = Menu(menu)
        menu.add_cascade(label="Courses", menu=course_menu)
        course_menu.add_command(label="Add Course", command=self.add_course_window)

        task_menu = Menu(menu)
        menu.add_cascade(label="To-Do", menu=task_menu)
        task_menu.add_command(label="Add Task", command=self.add_task_window)

        habit_menu = Menu(menu)
        menu.add_cascade(label="Habits", menu=habit_menu)
        habit_menu.add_command(label="Add Habit", command=self.add_habit_window)

        activity_menu = Menu(menu)
        menu.add_cascade(label="Activities", menu=activity_menu)
        activity_menu.add_command(label="Add Activity", command=self.add_activity_window)

        # Labels and Buttons for each section
        Label(root, text="Welcome to TaskMaster!", font=("Arial", 20), bg="#f2f2f2", fg="#4b4b4b").pack(pady=20)

        # List all tasks
        Button(root, text="View To-Do List", command=self.view_todo, bg="#4CAF50", fg="white").pack(pady=5)

        # Reminder System (for all upcoming deadlines)
        Button(root, text="View Assignments & Reminders", command=self.view_assignments, bg="#4CAF50", fg="white").pack(pady=5)

    def add_course_window(self):
        win = Toplevel()
        win.title("Add Course")
        win.configure(bg="#f2f2f2")
        Label(win, text="Course Name", bg="#f2f2f2").pack()
        course_name_entry = Entry(win)
        course_name_entry.pack()
        Label(win, text="Schedule", bg="#f2f2f2").pack()
        schedule_entry = Entry(win)
        schedule_entry.pack()
        Button(win, text="Add", command=lambda: add_course(course_name_entry.get(), schedule_entry.get())).pack(pady=10)

    def add_task_window(self):
        win = Toplevel()
        win.title("Add Task")
        win.configure(bg="#f2f2f2")
        Label(win, text="Task Name", bg="#f2f2f2").pack()
        task_name_entry = Entry(win)
        task_name_entry.pack()
        Label(win, text="Category", bg="#f2f2f2").pack()
        category_entry = Entry(win)
        category_entry.pack()
        Label(win, text="Priority", bg="#f2f2f2").pack()
        priority_entry = Entry(win)
        priority_entry.pack()
        Label(win, text="Due Date (YYYY-MM-DD)", bg="#f2f2f2").pack()
        due_date_entry = Entry(win)
        due_date_entry.pack()
        Button(win, text="Add", command=lambda: add_todo(task_name_entry.get(), category_entry.get(),
                                                         int(priority_entry.get()), due_date_entry.get())).pack(pady=10)

    def add_habit_window(self):
        win = Toplevel()
        win.title("Add Habit")
        win.configure(bg="#f2f2f2")
        Label(win, text="Habit Name", bg="#f2f2f2").pack()
        habit_name_entry = Entry(win)
        habit_name_entry.pack()
        Label(win, text="Start Date (YYYY-MM-DD)", bg="#f2f2f2").pack()
        start_date_entry = Entry(win)
        start_date_entry.pack()
        Label(win, text="Frequency (days)", bg="#f2f2f2").pack()
        frequency_entry = Entry(win)
        frequency_entry.pack()
        Button(win, text="Add", command=lambda: add_habit(habit_name_entry.get(),
                                                          start_date_entry.get(),
                                                          int(frequency_entry.get()))).pack(pady=10)

    def add_activity_window(self):
        win = Toplevel()
        win.title("Add Activity")
        win.configure(bg="#f2f2f2")
        Label(win, text="Activity Name", bg="#f2f2f2").pack()
        activity_name_entry = Entry(win)
        activity_name_entry.pack()
        Label(win, text="Event Date (YYYY-MM-DD)", bg="#f2f2f2").pack()
        event_date_entry = Entry(win)
        event_date_entry.pack()
        Button(win, text="Add", command=lambda: add_activity(activity_name_entry.get(), event_date_entry.get())).pack(pady=10)

    def view_todo(self):
        todos = get_todos()
        win = Toplevel()
        win.title("To-Do List")
        for task in todos:
            Label(win, text=f"Task: {task[1]}, Category: {task[2]}, Priority: {task[3]}, Due: {task[4]}").pack()

    def view_assignments(self):
        assignments = get_assignments()
        win = Toplevel()
        win.title("Assignments & Reminders")
        for assignment in assignments:
            Label(win, text=f"Assignment: {assignment[2]}, Due: {assignment[3]}, Grading: {assignment[4]}").pack()


# Main loop
if __name__ == "__main__":
    initialize_db()
    root = Tk()
    app = TaskMasterApp(root)
    root.mainloop()

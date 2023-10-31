import sqlite3
from task import Task
import datetime

date = datetime.datetime


connection = sqlite3.connect('./db/sqlite.db',check_same_thread=False)
cursor = connection.cursor()
class Persistence:

    def __init__(self, tasks):
        self.tasks = tasks

    def insertTasks(self):
        tasks : list = self.tasks
        cursor.execute("DELETE FROM tasks")
        for index in range(0, len(tasks)):
            task : Task = tasks[index]
            cursor.execute("INSERT INTO tasks VALUES ('{}', '{}', '{}', '{}', {}, {}); ".format(task.label, task.description, task.category, task.deadline, task.done, task.deadline_marked))
        connection.commit()

    def getAllTasks(self):
        for row in cursor.execute('SELECT * FROM tasks'):
            task_label : str = row[0]
            task_description : str = row[1]
            task_category : str = row[2]
            task_deadline : datetime = date.strptime(row[3], "%Y-%m-%d %H:%M:%S")
            task_done : bool = row[4]
            task_deadline_marked : bool = row[5]
            new_task : Task = Task(task_label, task_description, task_category, task_deadline, task_done, task_deadline_marked)
            self.tasks.append(new_task)
        
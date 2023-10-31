from task import Task

import datetime

from tkinter import messagebox

date = datetime.datetime

class TaskMonitor:
    def __init__(self, tasks : list):
        self.tasks = tasks
    
    def showTaskScheduleAlert(self, label : str, description : str, deadline : datetime):
        messagebox.showinfo("Lembrete para a tarefa {}".format(label), "A tarefa {}, com a descrição {}, está com um lembrete para {}".format(label, description, deadline))

    def monitor(self):
        tasks : list = self.tasks
        while True:
            if len(tasks) > 0:
                for index in range(0, len(tasks)):
                    task : Task = tasks[index]
                    task_deadline : datetime = task.deadline
                    task_done : bool = task.done
                    if(task_done==False):
                        while True:
                            current_datetime : datetime = date.now()
                            diff = (task_deadline - current_datetime).total_seconds()
                            if(task_done==False):
                                if diff <= 0:
                                    self.showTaskScheduleAlert(task.label, task.description, task.deadline)
                                    tasks[index].deadline_marked = True
                                    break
import datetime

class Task:
    def __init__(self,label : str, description : str, category : str, deadline : datetime, done: bool, deadline_marked: bool):
        self.label = label
        self.description = description
        self.category  = category
        self.deadline = deadline
        self.done = done
        self.deadline_marked = deadline_marked
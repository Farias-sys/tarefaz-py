import datetime
from console_interface import ConsoleInterface
from task_monitor import TaskMonitor
from persistence import Persistence
import threading

date = datetime.datetime

if __name__ == '__main__':
    tasks : list = []

    persistence = Persistence(tasks)
    persistence.getAllTasks()

    console_interface = ConsoleInterface(tasks)
    task_monitor = TaskMonitor(tasks)

    thread_monitor = threading.Thread(target=task_monitor.monitor)
    thread_menu = threading.Thread(target=console_interface.optionsPanel)

    thread_monitor.start()
    thread_menu.start()
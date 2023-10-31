import datetime
from task import Task
from console_interface import ConsoleInterface
from task_monitor import TaskMonitor
import threading

date = datetime.datetime

tasks : list = []

console_interface = ConsoleInterface(tasks)

task_monitor = TaskMonitor(tasks)

thread_menu = threading.Thread(target=console_interface.optionsPanel)
thread_monitor = threading.Thread(target=task_monitor.monitor)

thread_menu.start()
thread_monitor.start()


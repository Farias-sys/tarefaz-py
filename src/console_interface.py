from task import Task
import datetime
from pyfiglet import Figlet
import os
from utils import Utils
from persistence import Persistence

f = Figlet(font='3-d')

date = datetime.datetime

class ConsoleInterface:
    def __init__(self, tasks : list):
        self.tasks = tasks

    def showDetailedTask(self, task_array_id : int):

        task_array_id-=1
        task : Task = self.tasks[task_array_id]

        os.system('cls')
        print("----------------------------")
        print("Nome da tarefa: {}".format(task.label))
        print("Categoria da tarefa: {}".format(task.category))
        print("Descrição da tarefa: {}".format(task.description))
        print("Data limite da tarefa: {}".format(date.strftime(task.deadline, "%d/%m/%Y, %H:%M:%S")))
        print("Feita: {}".format("Sim" if task.done == True else "Não"))
        print("----------------------------")
        print("O que deseja fazer nesta tarefa? ")
        print("----------------------------")
        print("1 - Marcar como concluída")
        print("2 - Deletar tarefa")
        print("3 - Adiar ou adiantar tarefa")
        print("4 - Voltar ao menu de tarefas")
        print("----------------------------")
        

        while True:
            try:
                option : int = int(input("Opção escolhida: "))
                if option == 1:
                    self.tasks[task_array_id].done = True
                    print("Tarefa marcada como concluída!")
                    self.returnToOptionsPanel()
                    break
                elif option == 2:
                    del self.tasks[task_array_id]
                    persistence = Persistence(self.tasks)
                    persistence.insertTasks()
                    print("Tarefa deletada!")
                    self.returnToOptionsPanel()
                    break
                elif option == 3:
                    self.tasks[task_array_id].deadline = date.strptime(str(input("Digite a data para conclusão da tarefa(Formato DD/MM/AAAA HH:MM): ")), "%d/%m/%Y %H:%M")
                    print("Tarefa alterada!")
                    self.returnToOptionsPanel()
                    break
                elif option == 4:
                    self.showTasks()
                    break
                else: 
                    print("Digite uma opção válida!")
            except ValueError:
              print('Digite um número!')

    @property
    def showTasks(self):

        tasks : list = self.tasks

        os.system('cls')
        print("{} Tarefas encontradas".format(len(tasks)))

        for index in range(0, len(tasks)):
            task : Task = tasks[index]
            task_array_id : int = index + 1
            task_label : str = task.label
            task_deadline : str = date.strftime(task.deadline, "%d/%m/%Y, %H:%M:%S")
            task_done : str = "Sim" if task.done == True else "Não"
            print("----------------------------")
            print("ID - NOME DA TAREFA - DATA PARA CONCLUSÃO - CONCLUÍDA")
            print("{} - {} - {} - {}".format(task_array_id, task_label, task_deadline,task_done))
            print("----------------------------")
            

        if len(tasks) > 0:
            while True:
                try:
                    print("----------------------------")
                    option : int = int(input("Digite o número da tarefa que deseja explorar ou 0 para voltar ao menu: "))
                    if option == 0:
                        self.optionsPanel()
                        break
                    elif option > 0 and option <= len(tasks):
                        self.showDetailedTask(option)
                        break
                    else:
                        print("Esta tarefa não existe!")
                        pass
                    print("----------------------------")
                except ValueError:
                  print('Digite um número!')
        else:
            self.returnToOptionsPanel()

    @property
    def createNewTask(self):

        os.system('cls')
        print("----------------------------")
        print("Criar nova tarefa")
        print("----------------------------")
        
        label : str = str(input("Digite o nome da tarefa: "))
        description : str = str(input("Digite uma descrição para a tarefa: "))
        category : str = str(input("Digite a categoria da tarefa: "))
        while True:
            try:
                deadline : str = str(input("Digite a data para conclusão da tarefa(Formato DD/MM/AAAA HH:MM): "))
                deadline_converted : datetime = date.strptime(deadline, "%d/%m/%Y %H:%M")

                if (deadline_converted - date.now()).total_seconds() < 0:
                    os.system('cls')
                    print("\n----------------------------")
                    print("A data para conclusão não pode ser anterior a data atual!")
                    print("Criar nova tarefa")
                    print("----------------------------\n")
                    pass
                else:
                    break   
            except ValueError:
                os.system('cls')
                print("\n----------------------------")
                print("Digite o valor correto!")
                print("Criar nova tarefa")
                print("----------------------------\n")
                
        
        new_task : Task = Task(label, description, category, deadline_converted, False, False)
        self.tasks.append(new_task)
        
        persistence = Persistence(self.tasks)
        persistence.insertTasks()

        print("Tarefa criada!")
        self.returnToOptionsPanel()

    @property
    def listCategories(self):

        tasks : list = self.tasks
        categories : list = []

        for index in range(0, len(tasks)):
            task : Task = tasks[index]
            categories.append(task.category)

        parsed_categories : list = Utils.remove_dups(categories)

        os.system('cls')
        print("----------------------------")
        print("{} Categorias encontradas".format(len(parsed_categories)))
        print("----------------------------")

        for index in range(0, len(parsed_categories)):
            print("{} - {}".format(index+1, parsed_categories[index]))
            print("----------------------------")

        self.returnToOptionsPanel()

    @property
    def returnToOptionsPanel(self):
        while True:
            try:
                option = input("Aperte ENTER para voltar ao painel")
                self.optionsPanel()
                break
            except:
                raise        

    def optionsPanel(self):

        os.system('cls')
        print(f.renderText("TarefaZ"))
        print("----------------------------")
        print("1 - Listar tarefas")
        print("2 - Cadastrar nova tarefa")
        print("3 - Listar categorias")
        print("----------------------------")

        while True:
            try:
                option : int = int(input("Escolha uma opção: "))
                if option == 1:
                    self.showTasks()
                    break
                elif option == 2:
                    self.createNewTask()
                    break
                elif option == 3:
                    self.listCategories()
                    break
                else:
                    print("Digite uma opção válida!")
                    pass
            except ValueError:
                print('Digite um número!')
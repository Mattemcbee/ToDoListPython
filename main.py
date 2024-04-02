from task import NewTask

class ToDoList:
  def __init__(self):
    self.task_list = []
  def add_task_to_list(self, name, description):
    task = NewTask(name, description)
    self.task_list.append(task)
  def view_tasks(self):
    print('To Do List: \n')
    for index, task in enumerate(self.task_list, start=1):
      print(f'{index}. {task.name} - {task.description}')
    print('\n')
  def delete_task(self):
    while True:
      toDelete=input('which do you want to delete?')
      taskToDelete=self.task_list[int(toDelete)-1]
      confirm=input(f'are you sure you want to delete {taskToDelete.name} - {taskToDelete.description}? (y/n)')
      if confirm.lower()=='y':
        del self.task_list[int(toDelete)-1]
        for index, task in enumerate(self.task_list, start=1):
          print(f'{index}. {task.name} - {task.description}')
        break
      elif confirm.lower()=='n':
        print('nothing deleted...')
        break

to_do = ToDoList()
option_list = ['1. Add Task', '2. View Task','3. Delete Task', '4. Exit']
options_text = '\n'.join(option_list)

def menu():
  is_on = True
  while is_on:
    choice = input(f'What would you like to do: \n{options_text}\n')

    if choice == '1':
      name = input('Enter the task name: ')
      description = input('Enter the task description: ')
      to_do.add_task_to_list(name, description)
      #print(len(to_do.task_list))
    elif choice == '2':
      #print(len(to_do.task_list))
      to_do.view_tasks()
    elif choice == '3':
        #print(len(to_do.task_list))
        to_do.delete_task()
    elif choice == '4':
      print('Exiting...')
      is_on = False
    else:
      print('Invalid choice. Please try again.')

if __name__ == "__main__":
    menu()

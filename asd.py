def save(tasks_list):
    file = open("toDoList.txt", "w+")
    for task in tasks_list:
        file.writelines(task + "\n")
    file.close()

def show_list(tasks_list):
    i = 1
    for task in tasks_list:
        print(str(i) + ". " + task)
        i+=1

def add_task(tasks_list):
    task = input("Zadanie: ")
    tasks_list.append(task)
    print("Zadanie zostało dodane.")

def delete(tasks_list):
    elem_to_del = int(input("Element do usuniecia: "))
    elem_to_del -=1 
    if elem_to_del < 0 or elem_to_del > len(tasks_list)-1:
        print("Podano nieprawidłowy index!")
    else:
        tasks_list.pop(elem_to_del)
        print("Usunięto zadanie")

def load_tasks_from_file(tasks_list):
    try:
        file=open("toDoList.txt")
        for line in file.readlines():
          tasks_list.append(line.strip())
        file.close()
    except FileNotFoundError:
        return

user_choice=-1
tasks = []

load_tasks_from_file(tasks)

while user_choice != 5:
    if user_choice == 1:
        add_task(tasks)
    elif user_choice == 2:
        delete(tasks)
    elif user_choice == 3:
        show_list(tasks)
    elif user_choice == 4:
        save(tasks)
    else:
        break

    print("\nStwórz swoją toDo listę")
    print("------------------------")
    print("Instrukcja obsługi:")
    print("1. Dodaj do listy \n2. Usuń z listy \n3. Wyświetl listę \n4.Zapisz zmiany do pliku. \n5.Zakończ")
    print("------------------------")

    user_choice=int(input("Podaj numer:"))

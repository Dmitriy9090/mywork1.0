HELP = """Доступные команды: 
help - вывести справку
show - показать добавленные задачи
add - добавить задачу""" # Выдаваемая справка при вводе комманды help


today = [] # дела на сегодня
tomorrow = [] # дела на завтра
other = [] # другие дела

while True:
    command = input("Введите команду: ") # Ввод необходимой команды
    if command == "help": # Ввод команды "помощь"
        print(HELP) # вывод справки HELP
    elif command == "add": # Ввод команды "Добавить задачу"
        date = input("Введите дату: ") # Ввод даты
        task = input("Введите задачу: ") # Ввод самой задачи
        if date == "Сегодня":
            today.append(task)
        elif date == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print(f"Задача {task} добавлена")
    elif command == "show":
        print("Сегодня")
        print (today)
        print ("Завтра")
        print (tomorrow)
        print ("Другие")
        print (other)
    elif command == "exit":
        print ("Спасибо за использование. До свидания!")
        break
    else:
        print("Неизвестная команда!")
        break
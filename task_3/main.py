import json
import os
choice = 0
filename = 'records.json'
with open(filename, 'r+', encoding="utf-8") as file:
    content = json.loads(file.read())

while choice != 5 :
    print("___________-М-Е-Н-Ю-___________")
    print("1.Вывести все записи")
    print("2.Вывести запись по полю ")
    print("3.Добавить запись ")
    print("4.Удалить запись по полю")
    print("5.Выйти из программы")
    print("________________________________")
  
    choice = int(input("Введите номер пункта: "))

    if choice == 1:
        print("----------------ВСЕ-ЗАПИСИ----------------")
        count = 1
        for information in content:
            print(f"----------{count}-ЗАПИСЬ-------------")
            for paragraph in information:
                print(f"{paragraph} : {information[paragraph]} ")
            count += 1

    elif choice == 2:
        print("--------------------------------------")
        id = input("введите поле (id): ")
        for information in content:
            if information['id'] == id:
                print(f"----------{id}-ЗАПИСЬ-------------")
                for paragraph in information:
                    print(f"{paragraph} : {information[paragraph]} ")

    elif choice == 3:
        print("-------------ВВОД-СТРОКИ-----------")
        id = input("введите id:")
        name = input("введите name:")
        manufacturer = input("введите manufacturer:")
        

        

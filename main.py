import json

c = 0 #вводимый пункт
new_sity = {"id":0, "name":"", "country":"", "is_big":False,"people_count":0} #множество для добавляемой записи

with open('k.json', 'r', encoding='utf-8') as file: #открывается файл json и записывается в data
    data = json.load(file)

    while c != 5: #цикл повторяется пока пользователь не выберет 5(закрыть программу)
        k = 0 #переменная для нахождения порядка записи
        flag = True #флаг для проверки наличия записи
        print("1 - Вывести все записи\n2 - Вывести запись по полю\n3 - Добавить запись\n4 - Удалить запись по полю\n5 - Выйти из программы\n")
        c = int(input("Выберите действие(введите число): ")) #запрашивает действие пользователя в переменную
        
        if c == 1: #выводит все записи
            print("===========")
            for sity in data:
                print(f"{sity["id"]}: {sity["name"]}, {sity["country"]}\nНаселение: {sity["people_count"]}, >100000 ?: {sity["is_big"]}\n==========")
        
        elif c == 2:#выводит поле записи, id которой ввел пользователь
            inp_id = int(input("Введите поле выводимой записи: "))
            for sity in data:
                k += 1
                if inp_id == sity["id"]:
                    print(f"{sity["id"]}: {sity["name"]}, {sity["country"]}\nНаселение: {sity["people_count"]}, >100000 ?: {sity["is_big"]}\nПорядковый номер записи: {k}\n==========")
                    flag = False
            print("=====Запись не найдена======\n" if flag else "")
        
        elif c == 3: #ввод всех данных, запись их в множество и добавление множество в data
            new_sity["id"] = int(input("Введите id: "))
            new_sity["name"] = input("Введите название города: ")
            new_sity["country"] = input("Введите страну: ")
            new_sity["people_count"] = int(input("Введите население: "))
            new_sity["is_big"] = (True if new_sity["people_count"]>100000 else False)
            data.append(new_sity)
        
        elif c == 4: #находится id в файле, после чего запись с нужным id удаляется
            inp_id = int(input("Введите поле удаляемой записи: "))
            for sity in data:
                if inp_id == sity["id"]:
                    data.pop(k)
                    flag = False
                k += 1
            print("=====Запись не найдена======\n" if flag else "")
    
        
        elif c == 5: #завершается цикл
            print('Завершение работы программы')
            break
        
        else: #при вводе некорректного значения
            print('Введите корректное значение')

with open('k.json', 'w', encoding='utf-8') as file: #информация записывается обратно в файл
    json.dump(data, file, indent=4, ensure_ascii=True)

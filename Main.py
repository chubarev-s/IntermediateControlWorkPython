# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.

import datetime
import json
import os

def main():
    count = 2
    print("Добро пожаловать в заметки! \n" 
            "Выбериете действие: \n"
            "1 - Создать заметку, " 
            "2 - Найти нужную заметку, "
            "3 - Редактирование заметки, "
            "4 - Удалить заметку. " 
            "5 - Показать список всех заметок")
    
    select = int(input())
    if select == 1:
        print("Введите название заметки: ")
        notesName = input() + ".json"
        print("Введите заметку: ")
        note = input()
        add_note(notesName, note, 1)
        print("Заметка успешно создана! \n")
    
    elif select == 2:
        print("Введите название заметки: ")
        nameNote = input()
        notesName = "IntermediateControlWorkPython/notes/" + nameNote + ".json"
        noteOpen = open(notesName, encoding='utf-8')
        readNote = noteOpen.read()
        print(f"Вы открыли заметку: {nameNote} \n" + "----------------------------------------------------\n")
        print(readNote)

    elif select == 3:
        print("Введите название заметки: ")
        nameNote = input() + ".json"
        print("Введите текст заметки: \n")
        note = input()
        add_note(nameNote, note, count)
        print("Заметка изменена.")
        count = count + 1


    elif select == 4:
        print("Введите название заметки: ")
        nameNote = input()
        notesName = "IntermediateControlWorkPython/notes/" + nameNote + ".json"
        print(f"Вы точно хотите удалить \"{nameNote}\"?\n" 
              "Введите 1 если да, 2 если нет")
        chose = int(input())
        if chose == 1:
            os.remove(notesName)
            print("Заметка успешно удалена!")
        else:
            print("Уффффф, успели, заметка осталась в Вашей памяти!")

    elif select == 5:
        searchDir = "IntermediateControlWorkPython/notes/"
        search = os.listdir(searchDir)
        noteSearch = []
        for file in search:
            if os.path.isfile(os.path.join(searchDir, file)) and file.endswith('.json'):
                noteSearch.append(file)
        print("Созданные заметки: " + str(noteSearch))


#метод создания заметки в формате json
def add_note(notesName, note, n):
    noteFile = os.path.join("IntermediateControlWorkPython/notes", notesName)
    from datetime import datetime
    date = datetime.now()
    dateJSON = str(date)
    note = str(note)
    data = {
        "id": n,
        "text": note,
        "date": dateJSON
        }
    with open(noteFile, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.write("\n")

main()






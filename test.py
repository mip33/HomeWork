documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def move_shelf():
    tmp = None
    doc_arg = input('Введите номер документа:')
    for key,value in directories.items():
        if doc_arg in value:
            i = value.index(doc_arg)
            tmp = value.pop(i)
            break
    if tmp is None:
        print("Документ не найдена!")
        return
    num_shelf = input('Введите номер полки:')
    if num_shelf not in directories:
        print("Полка не найдена!")
        return
    directories[num_shelf].append(tmp)
    print("Документ добавлен на полку")


def add_shelf():
    num_shelf = input('Введите номер полки:')
    if num_shelf in directories:
        print("Полка уже существует!")
        return
    directories[num_shelf] = []
    print('Полка добавлена')

move_shelf()
add_shelf()


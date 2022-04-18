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




def people_doc(doc_arg):
    for document in documents:
        if document['number'] == doc_arg:
            print('Владелец: ', document['name'])
            break
    else:
        print('Внимание! Такого документа - нет в архиве.')


def shel_num(doc_arg):
    for key,value in directories.items():
        if doc_arg in value:
            print(key)
            break
    else:
        print('Внимание! Такого документа - нет в архиве.')


def all_list():
    for document in documents:
        print('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))

def add_new_user(type_doc, num_doc, name, num_shel):
    if int(num_shel) == 1 or int(num_shel) == 2 or int(num_shel) == 3:                                                              
            documents.append({'type': type_doc, 'number':num_doc,'name':name})
            directories[num_shel].append(num_doc)
            print(f'Ваш документ добавлен на полку № {num_shel}')
    else:
        print(f"Такой полки нет")

def main_menu():
    while True:
        command = input('\n Выберете одну из команд: p, l, s, a\n\
                            Для выхода наберите: exit или q \n\
                            Для вызова справки наберите: help или h \n\
                            Введите команду: ')
        if command == 'p':
                    people_doc(input('\nВведите номер документа: '))
        elif command == 'l':
                    all_list()
        elif command == 's':
                    shel_num(input('\nВведите номер документа: '))
        elif command == 'a':
            add_new_user(input('Тип документа:'),input("Номер документа"),input("Имя:"),input("Номер полки"))
        elif command == 'exit' or command == 'q':
              break
        elif command == 'help' or command == 'h':
            print('\n \
    p – команда, которая по номеру документа выведет имя, владельца;\n \
    l – команда, которая выведет список всех документов;\n \
    s – команда, которая по номеру документа выведет номер полки, на которой он находится;\n \
    a – команда, которая добавит новый документ в архив;\n \
    d - команда, которая по номеру документа удалит его из каталога и из перечня полок;\n \
    m - команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;\n \
    as - команда, которая спросит номер новой полки и добавит ее в перечень.')
        else:
            print('Вы ввели команду не корректно, повторите ввод.')

main_menu()
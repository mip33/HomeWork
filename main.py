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


def delete(doc_arg):
    found = None
    for i,document in enumerate(documents):
        if document['number'] == doc_arg:
            found = i
            documents.remove(document)
            break
    # if found:
    #     documents.pop(found)
    #     print('Документ № ', doc_arg, 'удален')
    # else:
    #     print('Документ не найден')

    for dir in directories.values():
        if doc_arg in dir:
            dir.remove(doc_arg)
            print('Домумент удален c полки')

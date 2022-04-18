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

def move_shelf(doc_arg):
    tmp = None
    for key,value in directories.items():
        if doc_arg in value:
            i = value.index(doc_arg)
            tmp = value.pop(i)
            break
    




move_shelf(11-2)
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
# def people():
#     num_doc = input('Введите номер документа:')
#     for i in documents:
#         if num_doc in i.values():
#             print(i['name'])


# def shelf():
#     num_doc = input('Введите номер документа:')
#     for j,k in directories.items():
#         if num_doc in k:
#             print(j)
# def list():
#     for i in documents:
#         print( '''{} "{}" "{}"'''.format(i['type'],i['number'],i['name']))


def add():
    num_doc = input("Введите № дока:")
    type_doc = input("Введите тип дока:")
    name = input("Введите имя:")
    dir_num = int(input("Введите № полки"))
    if directories.keys() == dir_num:
        for key,value in documents:
            documents.append(f' "type":{type_doc}, "number":{num_doc}, "name":{name}')
            print(documents)

add()
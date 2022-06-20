# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
# Техническое задание
# Количество передаваемых имен в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Вернуть словарь с ключами, отсортированными в алфавитном порядке.
# Примеры/Тесты:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
# Алгоритм
# Вспомните как обработать произвольное количество передаваемых параметров.

def thesaurus(some_list):
    for name in some_list:
        if name[0] in dict1:
            dict1.get(name[0]).append(name)  # !!!! очень интересное свойство
        else:
            dict1[name[0]] = [name]
    for key in sorted(dict1.keys()):
        print(f'\t{key}:  {dict1[key]}')


dict1 = {}
some_list = ["Иван", "Мария", "Петр", "Илья", "Кирилл", "Маша", "Алексей"]

thesaurus(some_list)
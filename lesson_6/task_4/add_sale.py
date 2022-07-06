# 4. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# Техническое задание:
# Все файлы этого задания хранить в отдельной директории, наример «task_4» или другое.
# Данные хранить в файле bakery.csv в кодировке utf-8.
# Соблюдаем формат данных в файле: одна запись (цифра) это одна строка.
# Добавление записи
# Имя исполняемого скрипта: add_sale.py
# При записи передавать из командной строки значение суммы продаж. Функцию input не использовать.
# Новая запись дозаписывается в конец файла.
# Корректно обработать неправильное количество или тип переданных параметров.
# Чтение данных.
# Имя исполняемого скрипта: show_sales.py
# Предполагаем, что первая запись имеет номер 1.
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи от номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная от номера, равного первому числу, по номер,
# равный второму числу, включительно;
# Корректно обработать неправильное количество или тип переданных параметров.
# Примеры/Тесты:
# Примеры запуска скриптов:
#
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
#
# Алгоритм
#
# Для удобства отладки кода - разделите его на два этапа:
# отдельно отладьте алгоритм получения данных из командной строки: получение и обработка;
# и отдельно отлаживайте алгоритм работы с записями файла. На втором этапе «переданные параметры»
# можно сразу внести в код и не работать с командной строкой.
# Усложнение Подумать, как избежать чтения всего файла в память при реализации второго и третьего
# случаев чтения данных.


from sys import argv
from os.path import join

print('You added to sales file: ', argv[1:])
print('If you want to view the records, then execute in the console: \n'
      '"show_sales.py x" to view from "x" to the end of the records; \n'
      'or "show_sales.py x y" to view in the range from x to y.')

add_path = join('.', 'bakery.csv')
bakery = open(file=add_path, mode='at', encoding='utf-8')
for idx in argv[1:]:
    if idx.isnumeric(): # далее можно добавлять и иные условия и проверки (ограничимся такой)
        bakery.write(f'{idx}\n')
    else:
        print(f'"{idx}" - is not mumeric, check this data and add if necessary on the next input')
        continue
bakery.close()
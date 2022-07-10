# Практическое задание 7. "Файловая система. Исключения" [21.02.2022]
# Тема урока: Работа с файлами и директориями: копирование, перемещение, создание,
# рекурсивный обход директории. Работа с Исключениями.
#
# Для всех заданий этого урока:
#
# Для каждой задачи создайте свою папку, например «task_1» и т.п., и в ней храните данные для этой задачи.
# Ваш код должен работать на любой ОС: не используйте в качестве путей строки с слешами.

# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
# |  |--settings
# |  |--mainapp
# |  |--adminapp
# |  |--authapp
#
# Техническое задание
#
# Продумайте ситуацию, когда все или часть этих папок уже есть в директории.
# Выберите наиболее подходящую структуру данных для хранения имен папок так,
# чтобы легко расширить количество создаваемых папок, например до 100 папок.
# Примечание:
#
# Можно ли будет расширять конфигурацию и хранить данные о вложенных папках и файлах?

from os.path import join, exists
from os import mkdir, makedirs


job_dir = input('Введите название рабочей директории: ')
part_work = input('Введите названия папок, которые надо добавить в рабочую директорию (например: dir1 dir2): ')
path_job = join('.', job_dir)
if not exists(path_job):
    mkdir(path_job)
    keep_file = join(path_job, ".keep")
    f = open(keep_file, "w")
    f.close()
for part in part_work.split():
    path_part = join(path_job, part)
    if not exists(path_part):
        mkdir(path_part)
    keep_file = join(path_part, ".keep")
    f = open(keep_file, "w")
    f.close()
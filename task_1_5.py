# 1. Написать генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield,
# полностью истощить генератор.
# Формат вывода результата:
# Программа явно должна закончиться на StopIteration
# Техническое задание
# n - любое положительное число.
# Не путайте истощение итератора и печать его значений. Явно дойдите до StopIteration.
# Истощение генератора - любым удобным для вас способом. Например создаем генератор в программе,
# а истощаем руками в консоли или через цикл.
# Создание генератора сделайте внутри функции iterator_without_yield(n), принимающей аргументом n любое
# положительное число и возвращающей генератор.
# Примеры/Тесты:
#
# gen1 = iterator_without_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration
#
# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200. Все остальное как в основном задании.

def iterator_without_yield(n):
    gen_n = (num for num in range(1, n + 1, 2))
    while True:
        print(next(gen_n))


n = int(input('Погенерим и истощим? Введите n положительное число: '))
gen_n = iterator_without_yield(n)


# >>>> со звездочкой <<<<

def iterator_without_yield(n):
    gen_n = (num for num in range(1, n + 1, 2))
    while True:
        for num in range(1, n + 1, 2):
            if num**2 < 200:
                print(next(gen_n))


n = int(input('Погенерим и истощим? Введите n положительное число: '))
gen_n = iterator_without_yield(n)



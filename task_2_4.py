# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, …) и возвращающую курс этой валюты по отношению к рублю.
# Формат вывода результата:
#
# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
# Техническое задание
#
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. В каком формате
# возвращен ответ?
# Функция принимает два аргумента: строка с URL, куда стучимся и строку с кодом валюты (только одной).
# Возвращает результат числового типа, например float. Если в качестве аргумента передали код валюты, которого
# нет в ответе, вернуть объект None.
# Для извлечения данных использовать только методы объект str.
# Сделать работу функции не зависящей от того, в каком регистре был передан аргумент.
# Функция должна корректно обрабатывать любой код валюты. Правильность параметра url можно не проверять.
# Вводить коды валют с клавиатуры (input) необязательно.


from requests import get

def currency_rates(url, ):
    pass


from requests import get
response = get('http://geekbrains.ru')
print(type(response)) # <class 'requests.models.Response'>
print(dir(response))
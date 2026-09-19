some_var = 5  # Переменная хранит значение 5
del some_var  # del удаляет переменную

print('Тестовый текст:', 'test')
print('Число преобразовано в строку:', str(5))  # str() преобразует значение в строку
print('Число преобразовано в целое число:', int(5))  # int() преобразует значение в целое число

# Основные типы данных в Python

# str - строка, текстовые данные
name = 'Maksim'
print('Тип переменной name:', type(name))

# int - целое число
age = 25
print('Тип переменной age:', type(age))

# float - число с точкой
price = 10.5
print('Тип переменной price:', type(price))

# bool - логический тип: True или False
is_student = True
print('Тип переменной is_student:', type(is_student))

# NoneType - отсутствие значения
empty_value = None
print('Тип переменной empty_value:', type(empty_value))

# list - список, изменяемая коллекция значений
numbers = [1, 2, 3, 4, 5]
print('Тип переменной numbers:', type(numbers))

# tuple - кортеж, неизменяемая коллекция значений
coordinates = (10, 20)
print('Тип переменной coordinates:', type(coordinates))

# set - множество, коллекция уникальных значений
unique_numbers = {1, 2, 3, 3, 4}
print('Тип переменной unique_numbers:', type(unique_numbers))
print('Множество уникальных чисел:', unique_numbers)

# dict - словарь, хранит данные в формате ключ: значение
user = {
    'name': 'Maksim',
    'age': 25,
}
print('Тип переменной user:', type(user))

# complex - комплексное число
# complex — тип данных для комплексных (мнимых) чисел вида a + bj. 
# Используется в научных вычислениях, физике и обработке сигналов. 
# В веб-разработке применяется редко.
complex_number = 3 + 4j
print('Тип переменной complex_number:', type(complex_number))

# bytes - набор байтов
data = b'Hello'
print('Тип переменной data:', type(data))

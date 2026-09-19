# Практика по обработке исключений

# Задача 1: безопасное деление

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ошибка: деление на ноль'

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# Задача 2: ввод числа с проверкой

while True:
    try:
        age = int(input('Введите ваш возраст: '))
        if age < 0:
            raise ValueError('Возраст не может быть отрицательным')
        print('Ваш возраст:', age)
        break
    except ValueError as e:
        print('Ошибка:', e)
        print('Попробуйте ещё раз')

# Задача 3: работа со списком

def get_element(items, index):
    try:
        return items[index]
    except IndexError:
        return 'Ошибка: индекс выходит за границы списка'

print(get_element([10, 20, 30], 1))
print(get_element([10, 20, 30], 10))

# Задача 4: обработка нескольких типов ошибок

try:
    number = int(input('Введите число: '))
    result = 100 / number
    print('Результат:', result)
except ValueError:
    print('Вы ввели не число')
except ZeroDivisionError:
    print('Нельзя делить на ноль')

# Задание для самостоятельной работы:
# 1. Написать функцию, которая принимает два числа и возвращает их сумму.
# 2. Если пользователь ввёл не число, обработать ValueError.
# 3. Вывести сообщение, что программа завершилась корректно.

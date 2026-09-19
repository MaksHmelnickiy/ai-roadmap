# Циклы позволяют повторять один и тот же код несколько раз

# В Python есть 2 основных вида циклов:
# for - перебирает элементы коллекции или диапазон чисел


# 1. Цикл for
# for удобно использовать, когда заранее известно количество повторений
# или нужно перебрать элементы: список, строку, словарь или range.

for number in range(5):
    print('Число из range(5):', number) # 0 1 2 3 4

for i in range(5):
    if i !=3 and i != 4:
        print('Число после проверки:', i) # 0 1 2

# range(2, 5):
# 2 — начало диапазона (первое число, которое получит переменная number)
# 5 — конец диапазона, но оно не включается
for number in range(2, 5):
    print('Число из range(2, 5):', number)  # Выведет: 2, 3, 4


# 2. Перебор списка через for
fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print('Фрукт из списка:', fruit)


# Операторы в циклах
# break — сразу останавливает цикл
for number in range(10):
    if number == 3:
        break
    print('Число до break:', number)  # 0, 1, 2

# continue — пропускает текущую итерацию и переходит к следующей
for number in range(5):
    if number == 2:
        continue
    print('Число без пропуска:', number)  # 0, 1, 3, 4

# else — выполняется после цикла, если его не остановил break
for number in range(3):
    print('Число в цикле:', number)
else:
    print('Результат цикла:', 'Цикл завершился без break')

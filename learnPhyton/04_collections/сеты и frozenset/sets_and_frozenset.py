# Set и frozenset

# Set хранит только уникальные элементы
numbers = {1, 2, 2, 3, 4}
# numbers = set([1, 2, 2, 3, 4])  # Создание множества с помощью функции set().
print('Set:', numbers)

# frozenset — неизменяемая версия set
frozen_numbers = frozenset(numbers)
print('Frozenset:', frozen_numbers)

# Добавление в set
numbers.add(5)
print('После add:', numbers)

# Удаление из set
numbers.remove(1)
print('После remove:', numbers)

# Обновление set с помощью update и дописывает новые элементы, если их нет в set
numbers.update([6, 7, 7, 8])
print('После update:', numbers)

# Основные методы set
print('Размер set:', len(numbers))
print('Проверка наличия 3:', 3 in numbers)
print('Проверка наличия 10:', 10 in numbers)

numbers.discard(10)  # Удаляет элемент, если он есть, и не вызывает ошибку, если его нет
print('После discard:', numbers)

numbers.pop()  # Удаляет и возвращает любой элемент из set, обычно первый попавшийся
print('После pop:', numbers)

numbers.clear()  # Очищает set
print('После clear:', numbers)

# Операции с set
# | — объединение: элементы из обоих множеств без повторов
# & — пересечение: только общие элементы
letters = {'a', 'b', 'c'}
print('Объединение:', numbers | letters)
print('Пересечение:', numbers & letters)

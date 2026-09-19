# Lambda-функции в Python
# Lambda = анонимная функция, которая обычно используется коротко и быстро

# Простой пример
square = lambda x: x * x
print("Квадрат числа 5:", square(5))

# Lambda с двумя аргументами
add = lambda a, b: a + b
print("Сумма 3 и 4:", add(3, 4))

# Lambda для проверки числа
is_even = lambda n: n % 2 == 0
print("Число 10 четное?", is_even(10))
print("Число 7 четное?", is_even(7))

# Lambda в функции map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Квадраты чисел:", squares)

# Lambda в функции filter()
filtered = list(filter(lambda x: x > 2, numbers))
print("Числа больше 2:", filtered)

# Lambda в функции sorted()
words = ["banana", "apple", "pear"]
sorted_words = sorted(words, key=lambda word: word)
print("Сортировка слов:", sorted_words)

# Lambda с условием
max_value = lambda a, b: a if a > b else b
print("Большее число из 8 и 12:", max_value(8, 12))

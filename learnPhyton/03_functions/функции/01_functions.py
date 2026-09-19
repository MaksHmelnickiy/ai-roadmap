# Функции в Python

# Простая функция

def greet(name):
    print(f"Привет, {name}!")


greet("Аня")


# Функция с возвращаемым значением

def add(a, b):
    return a + b


result = add(5, 7)
print("Сумма:", result)


# Функция без параметров

def hello():
    print("Привет, мир!")


hello()


# Функция с параметрами по умолчанию

def welcome(name, age=18):
    print(f"Имя: {name}, возраст: {age}")


welcome("Иван")
welcome("Мария", 25)


# Функция, которая возвращает несколько значений

def get_user_info():
    name = "Петр"
    age = 30
    return name, age


user_name, user_age = get_user_info()
print(user_name, user_age)


def analyze_numbers(numbers):
    if not numbers:
        return 0, 0, 0

    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    print ('ddddd', minimum)
    for number in numbers:
        total += number
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    return total, minimum, maximum


sum_result, min_result, max_result = analyze_numbers([4, 7, 2, 9, 1, 5])
print("Сумма:", sum_result)
print("Минимум:", min_result)
print("Максимум:", max_result)

grades = [8, 10, 6, 9, 7, 12, 5, 11]

def analyze_grades(numbers):
    
    if not numbers:
        return 0,0,0
    
    average = 0
    count = 0
    good=0
    bad=0
    for i in numbers:
        print(average)
        average += i
        count+=1
        if i<7:
            bad +=1
        if i >= 10:
            good+=1
    return average / count, good, bad
average, good, bad = analyze_grades(grades)
print('average: ', average)
print('good: ', good)
print('bad: ', bad)


# Она получает список целых чисел и должна вернуть 4 значения:
# сумму всех положительных чисел;
# сумму всех отрицательных чисел;
# количество чётных чисел;
# количество нечётных чисел.

list_num = [5,-7,2,4,-8,1,13,2,2]

def analyze_numbers(numbers):
    if not numbers:
        return 0,0,0,0
    positive = 0
    negative = 0
    even =  0
    odd = 0
    for i in numbers:
        if i > 0:
            positive +=i
        if i < 0:
            negative +=i
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return positive,negative,even,odd
positive, negative, even, odd = analyze_numbers(list_num)

print("Положительные:", positive)
print("Отрицательные:", negative)
print("Чётные:", even)
print("Нечётные:", odd)
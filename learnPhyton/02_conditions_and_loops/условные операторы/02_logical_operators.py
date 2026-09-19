# Логические операторы помогают объединять и изменять условия

# В Python есть 3 основных логических оператора:
# and - и
# or - или
# not - не


# 1. Оператор and
# Условие с and будет True только если все части условия True
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print('Результат проверки:', 'Можно войти')
else:
    print('Результат проверки:', 'Войти нельзя')


# 2. Оператор or
# Условие с or будет True, если хотя бы одна часть условия True
is_admin = False
is_moderator = True

if is_admin or is_moderator:
    print('Доступ к панели:', 'Есть доступ')
else:
    print('Доступ к панели:', 'Нет доступа')


# 3. Оператор not
# not меняет значение на противоположное:
# True становится False, а False становится True
is_blocked = False

if not is_blocked:
    print('Статус пользователя:', 'Не заблокирован')
else:
    print('Статус пользователя:', 'Заблокирован')


# 4. Связка if not
# if not можно читать как "если НЕ"
is_happy = False

if not is_happy:
    print('Настроение:', 'not happy')


# if not часто используют для проверки пустых значений
user_name = ''

# Пустая строка считается False
if not user_name:
    print('Проверка имени:', 'Имя пользователя не указано')
else:
    print('Имя пользователя:', user_name)

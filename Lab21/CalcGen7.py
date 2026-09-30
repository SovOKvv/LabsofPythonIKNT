# Написать функцию-генератор, реализующую вычисление последовательности коров Нараяны.

def narayana_generator(limit):
    if limit <= 0:
        return

    a, b, c = 1, 1, 1

    for i in range(limit):
        if i < 3:
            yield 1
        else:
            next_val = c + a
            yield next_val
            a, b, c = b, c, next_val

while True:
    try:
        user_n = int(input('Введите длину последовательности: '))

        if user_n <= 0:
            print('Количество должно быть положительным')
            continue

        print('\nИтоговая последовательность: ')
        for num in narayana_generator(user_n):
            print(num, end=" ")
        break

    except ValueError:
        print('Ошибка')
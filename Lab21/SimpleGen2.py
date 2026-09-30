# Написать функцию-генератор, которая принимает на вход список целых чисел и
# порождает последовательность текущих максимумов.

def current_max(numbers):
    if not numbers:
        return

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        yield max_num

while True:
    try:
        user_input = int(input('Введите количество чисел: '))
        user_nums = list(map(int, input('Введите числа через пробел: ').split()))

        if len(user_nums) != user_input:
            print('Количество чисел не совпадает')
            continue


        print('Исходный список:\n', *user_nums)
        print('Список текущих максимумов:')

        for m in current_max(user_nums):
            print(m, end=" ")
        break

    except ValueError:
        print('Ошибка: введите целые числа')
        continue

# 7
# 1 3 2 5 4 10 7
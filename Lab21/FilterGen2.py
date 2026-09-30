# Написать функцию-генератор, которая осуществляет фильтрацию входной
# последовательности символов. На вход функции подается строка. Генератор должен
# порождать последовательность символов, которые удовлетворяют следующему условию:
# являются строчными буквами английского алфавита.

def function_gen(lines):
    dictionary = set('abcdefghijklmnopqrstuvwxyz')
    for line in lines:
        if line in dictionary:
            yield line


while True:
    try:
        user_str = input('Введите строку: ').strip()
        if len(user_str) < 1:
          print('Строка не может быть пустой')
          continue

        print(f'Исходная строка: {user_str}')

        result_str = ''.join(function_gen(user_str))

        if result_str:
          print(f'Строчные буквы: {result_str}')
        else:
          print('Строчных букв англ. алфавита не найдено')

        break

    except ValueError:
        print('Ошибка')
        continue

# PprivetПриветMmirМИР
# Дано имя файла и целое число N_size (> 1). Создать файл целых чисел с данным именем и
# записать в него N_size первых положительных четных чисел (2, 4, …).

print('Создание файла с именем и записи в него четных чисел\n')

while True:
    try:
        filename = str(input('Введите название файла: '))
        N_number = int(input('Введите целое число: '))
        if N_number > 1 and filename.strip() != '':
            break
        else:
            print('Неверно введены данные, повторите попытку.')
    except ValueError:
        print('Неверно введены данные, повторите попытку.')

filename += '.bin'

with open(filename, 'wb') as file:
    for n in range(1, N_number + 1):
        current_number = n * 2
        file.write(current_number.to_bytes(4, 'little'))
print(f'\nФайл "{filename}" создан с первыми {N_number} целыми числами.')

with open(filename, 'rb') as file:
    while True:
            data = file.read(4)
            if not data:
                break
            print(int.from_bytes(data, 'little'))

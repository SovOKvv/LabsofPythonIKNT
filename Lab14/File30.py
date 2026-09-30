# Дан файл целых чисел, содержащий четное количество элементов.
# Удалить из данного файла вторую половину элементов.

print('Удаление второй половины элементов файла\n')

numbers = []
count = 0

with open('File30.bin', 'rb') as file:
    while True:
            data = file.read(4)
            if not data:
                break
            numbers.append(int.from_bytes(data, 'little'))
            count += 1

if len(numbers) != 0:
    print(f'Количество исходных чисел: {count}')
    count = 0

    with open('File30.bin', 'wb') as file:
        for i in range(len(numbers) // 2):
            file.write((numbers[i]).to_bytes(4, 'little'))
            count += 1

    print(f'Количество чисел в новом файле {count}')
    print('\nРезультат сохранен в файл "File30.bin"')
else:
    print('В файле нет чисел, повторите попытку')

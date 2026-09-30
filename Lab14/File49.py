# Даны четыре файла целых чисел разного размера с именами SA, SB, SC, SD и строка SE.
# Создать новый файл с именем SE, в котором чередовались бы элементы исходных файлов с одним и тем же
# номером (как в задании File48). «Лишние» элементы более длинных файлов в результирующий файл не записывать.

print('Создание файла SE с чередованием 4х исходных\n')

files = ['SA.txt', 'SB.txt', 'SC.txt', 'SD.txt']
content = {}

for filename in files:
    with open(filename, 'r') as file:
        numbers = [line.strip() for line in file]
        content[filename] = numbers

count_number = min(len(v) for v in content.values())
print(f'Минимальное количество элементов = {count_number}')

with open('SE.bin', 'wb') as file:
    for i in range(count_number):
        file.write(int(content['SA.txt'][i]).to_bytes(4, 'little'))
        file.write(int(content['SB.txt'][i]).to_bytes(4, 'little'))
        file.write(int(content['SC.txt'][i]).to_bytes(4, 'little'))
        file.write(int(content['SD.txt'][i]).to_bytes(4, 'little'))

print('В файл "SE" сохранены чередующиеся элементы из файлов "SA", "SB", "SC", "SD"\n')

with open('SE.bin', 'rb') as file:
    while True:
            data = file.read(4)
            if not data:
                break
            print(int.from_bytes(data, 'little'))



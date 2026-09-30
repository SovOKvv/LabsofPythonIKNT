# Дан файл вещественных чисел. Создать файл целых чисел, содержащий номера всех локальных максимумов
# исходного файла в порядке возрастания (определение локального максимума дано в задании File19).

print('Создание файла, содержащего номера всех локальных максимумом исходного файла\n')

def find_local_max():
    with open('File21.txt', 'rb') as file:
        numbers = []
        for line in file:
            numbers.append(float(line.strip()))

    if len(numbers) < 3:
        print('В файле недостаточно чисел для поиска локальных максимумов')
        return

    local_max = []

    for i in range(1,len(numbers) - 1):
        if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
            local_max.append(i+1)

    with open('File21_local_max.bin', 'wb') as file:
        for number in local_max:
            file.write(number.to_bytes(4, 'little'))

    print('Номера найденых максимумов:', *local_max)
    print('Результат сохранен в файл "File21_local_max.bin"')

find_local_max()

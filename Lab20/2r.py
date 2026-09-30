# Последовательности длины n_len из чисел от 1 до k_numbs. Написать рекурсивную
# программу перечисления всех последовательностей длины n_len из чисел от 1 до k_numbs.
# Формат входных данных:
# Входные данные содержат одну строку, в которой находится два целых числа
# сначала n_len (0<n_len<12), потом k_numbs (0<k_numbs<5).
# Формат выходных данных:
# На выходе нужно получить все возможные последовательности из n_len чисел, где
# каждое число в пределах от 1 до k_numbs. Каждая последовательность должна быть
# выведена в отдельной строке. Числа в последовательность не нужно разделять
# пробелами. Последовательности нужно выводить в лексикографическом порядке.
print('Нахождение всех последовательностей из N\n')


class EnumerationSequences:
    def __init__(self, n_len, k_numbs, output_file):
        self.n_len = n_len
        self.k_numbs = k_numbs
        self.output_file = output_file

    def enumerate(self, current):
        if len(current) == self.n_len:
            self.output_file.write(''.join(map(str, current)) + '\n')
            return

        for num in range(1, self.k_numbs + 1):
            current.append(num)
            self.enumerate(current)
            current.pop()

def main():
    with open('input2r.txt', 'r', encoding='utf-8') as file:
        line = list(map(int, file.readline().strip().split()))
    n_len, k_numbs = int(line[0]), int(line[1])

    with open('output2r.txt', 'w', encoding='utf-8') as f:
        generator = EnumerationSequences(n_len, k_numbs, f)
        generator.enumerate([])

    print(f'Сгенерировано последовательностей')

if __name__ == "__main__":
    main()
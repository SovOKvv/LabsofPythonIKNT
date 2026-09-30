# Юный путешественник решил изучить схему авиационного сообщения Схема
# авиационного сообщения задана в текстовом файле с именем FileName. в виде матрицы
# смежности. Первая строка файла содержит количество городов (n) n<=25, связанных
# авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
# имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить номера
# городов, в которые из города K можно долететь менее чем с L пересадками. Перечислите
# номера таких городов в порядке возрастания. Нумерация городов начинается с 1. Если
# таких городов нет, выведите число (-1).

class RouteFinder:

    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.n = 0
        self.matrix = []
        self.k = 0
        self.l = 0
        self.reachable_cities = []

    def read_data(self):
        with open(self.input_filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        self.n = int(lines[0])

        self.matrix = []
        for i in range(1, self.n + 1):
            self.matrix.append(list(map(int, lines[i].split())))

        params = list(map(int, lines[self.n + 1].split()))
        self.k = params[0]
        self.l = params[1]

    def find_reachable_cities(self):
        start = self.k - 1
        distances = {}
        queue = [(start, 0)]
        distances[start] = 0

        head = 0
        while head < len(queue):
            curr, dist = queue[head]
            head += 1

            for nxt in range(self.n):
                if self.matrix[curr][nxt] == 1 and nxt not in distances:
                    distances[nxt] = dist + 1
                    queue.append((nxt, dist + 1))

        valid_indices = []
        for node, dist in distances.items():
            if 1 <= dist <= self.l:
                valid_indices.append(node)

        self.reachable_cities = sorted([node + 1 for node in valid_indices])

    def write_results(self):
        with open(self.output_filename, 'w') as f:
            if not self.reachable_cities:
                f.write('-1\n')
            else:
                f.write(' '.join(map(str, self.reachable_cities)) + '\n')

    def process(self):
        self.read_data()
        self.find_reachable_cities()
        self.write_results()


def main():
    finder = RouteFinder('graf5in.txt', 'graf5out.txt')
    finder.process()
    print('Поиск городов, достижимых менее чем с L пересадками\n')
    print('Результаты записаны в файл "graf5out.txt".')


if __name__ == '__main__':
    main()
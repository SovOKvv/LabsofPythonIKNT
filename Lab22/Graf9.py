# Юный путешественник решил изучить схему авиационного сообщения Схема
# авиационного сообщения задана в текстовом файле с именем FileName1. в виде матрицы
# смежности. Первая строка файла содержит количество городов (n) n<=15, связанных
# авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
# имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить сколько
# есть маршрутов из города К1 в город К2 с L пересадками. В файл с именем FileName2 в
# первой строке выведите число таких маршрутов, а в следующих строках перечислите все
# такие маршруты в лексикографическом порядке. Маршрут задается перечислением номеров
# городов, нумерация городов идет с 1. Если таких маршрутов нет, выведите число (-1).

class RouteFinder:
    """
    Класс для поиска всех авиамаршрутов из города K1 в город K2 с заданным количеством пересадок L.

    Attributes:
        input_filename (str): Имя входного файла с матрицей смежности и параметрами;
        output_filename (str): Имя выходного файла для сохранения результатов;
        n (int): Количество городов в графе;
        matrix (list[list[int]]): Матрица смежности;
        k1 (int): Город отправления;
        k2 (int): Город назначения;
        l (int): Количество пересадок;
        routes (list[list[int]]): Список найденных маршрутов в лексикографическом порядке.
    """
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.n = 0
        self.matrix = []
        self.k1 = 0
        self.k2 = 0
        self.l = 0
        self.routes = []

    def read_data(self):
        with open(self.input_filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        self.n = int(lines[0])

        self.matrix = []
        for i in range(1, self.n + 1):
            self.matrix.append(list(map(int, lines[i].split())))

        params = list(map(int, lines[self.n + 1].split()))
        self.k1 = params[0]
        self.k2 = params[1]
        self.l = params[2]

    def find_routes(self):
        """
        Поиск всех возможных маршрутов с L пересадками методом обхода в глубину и последующей
        сортировкой.
        """

        start = self.k1 - 1
        end = self.k2 - 1
        target_edges = self.l + 1

        def dfs(current_node, path):
            if len(path) == target_edges + 1:
                if current_node == end:
                    self.routes.append([node + 1 for node in path])
                return

            for next_node in range(self.n):
                if self.matrix[current_node][next_node] == 1:
                    dfs(next_node, path + [next_node])

            dfs(start, [start])
            self.routes.sort()

    def write_results(self):
        with open(self.output_filename, 'w') as f:
            if not self.routes:
                f.write('-1\n')
            else:
                f.write(f'{len(self.routes)}\n')
                for route in self.routes:
                    f.write(' '.join(map(str, route)) + '\n')

    def process(self):
        self.read_data()
        self.find_routes()
        self.write_results()


def main():
    finder = RouteFinder('graf9in.txt', 'graf9out.txt')
    finder.process()
    print('Нахождение маршрутов из города K1 в город K2 c L пересадками\n')
    print('Результаты записаны в файл "graf9out.txt".')


if __name__ == '__main__':
    main()
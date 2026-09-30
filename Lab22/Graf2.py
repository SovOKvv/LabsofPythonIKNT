# Дано описание неориентированного графа в текстовом файле с именем FileName1. В виде матрицы смежности.
# Первая строка файла содержит количество вершин графа(n),а следующие n строк содержат матрицу смежности (a),
# a[i][j]=0, если ребра между вершинами i и j не существует. Построить матрицу инцидентности данного графа
# и вывести ее в файл с именем FileName2. Для справки: матрица инцидентности(b) имеет размер n x m, m - число
# ребер графа, b[i][j]=1, если ребро j инцидентно вершине i,в противном случае b[i][j]=0. Нумерацию ребер
# осуществлять в следующем порядке:сначала ребра, инцидентные вершине номер 1, потом ребра инцидентные вершине
# номер 2 и т.д. до вершины номер n. Ребра, инцидентные вершине с номером i перечислять в порядке возрастания
# номера второй вершины, инцидентной данному ребру. При выводе в первой строке указать размер матрицы инцидентности:
# числа n и m, а в следующих n строках разместить матрицу инцидентности.

class Graph:
    """
    Класс для представления графа и преобразования матрицы смежности в матрицу инцидентности.

        Attributes:
            n_vert (int): Количество вершин в графе;
            adj_matrix (list[list[int]]): Матрица смежности графа;
            edges (list[tuple[int, int]]): Список ребер графа в отсортированном порядке;
            incidence_matrix (list[list[int]]): Матрица инцидентности.
    """

    def __init__(self):
        self.n_vert = 0
        self.adj_matrix = []
        self.edges = []
        self.incidence_matrix = []

    def read_adjacency_matrix(self, filename):
        """
        Чтение матрицы смежности из текстового файла.

            Args:
                filename (str): Имя входного файла с матрицей смежности.
        """
        with open(filename, 'r') as f:
            lines = f.readlines()
        self.n_vert = int(lines[0].strip())
        self.adj_matrix = [list(map(int, lines[i].split())) for i in range(1, self.n_vert + 1)]

    def extract_edges(self):
        """Извлечение и сортировка ребер из матрицы смежности."""
        self.edges = []
        for i in range(self.n_vert):
            for j in range(i + 1, self.n_vert):
                if self.adj_matrix[i][j]:
                    self.edges.append((i, j))
        self.edges.sort()

    def build_incidence_matrix(self):
        """Построение матрицы инцидентности на основе списка ребер."""
        m = len(self.edges)
        self.incidence_matrix = [[0] * m for _ in range(self.n_vert)]
        for idx, (u, v) in enumerate(self.edges):
            self.incidence_matrix[u][idx] = 1
            self.incidence_matrix[v][idx] = 1

    def write_incidence_matrix(self, filename):
        """
        Запись матрицы инцидентности в текстовый файл.
            Args:
                filename (str): Имя выходного файла для сохранения матрицы.
        """

        with open(filename, 'w') as f:
            f.write(f'{self.n_vert} {len(self.edges)}\n')
            for row in self.incidence_matrix:
                f.write(' '.join(map(str, row)) + '\n')

    def process(self, input_filename, output_filename):
        """
        Метод для полной обработки графа.

            Args:
                input_filename (str): Имя файла с матрицей смежности.
                output_filename (str): Имя файла для сохранения матрицы инцидентности.
        """
        self.read_adjacency_matrix(input_filename)
        self.extract_edges()
        self.build_incidence_matrix()
        self.write_incidence_matrix(output_filename)


def main():
    Graph().process('graf2in.txt', 'graf2out.txt')
    print('Матрицы инцидентности сохранена в файле "graf2out.txt"')

if __name__ == "__main__":
    main()
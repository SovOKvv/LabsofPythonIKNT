# Задача вывода путника из лабиринта. Дан лабиринт размером NхN (N<=15).
# Форма лабиринта записана в текстовом файле, стена обозначается символом М, отсутствие
# стены - символом пробела. Даны координаты путника в лабиринте (номер строки (X) и номер
# столбца (Y)). Нужно вывести самый короткий путь выхода из лабиринта. Путь вывести в виде
# строки символов направлений. Возможные направления: L - влево, R - вправо, U - вверх, D -
# вниз. Гарантируется, что самый короткий путь только один. Длина пути определяется числом
# клеток, на которые должна ступить нога путника.
print('Вывод путника из лабиринта')
print('(ввод старта начинается с x = 1, y = 1)\n')

class Maze:
    def __init__(self, filename):
        with open(filename, 'r') as file:
            lines = [line.rstrip('\n') for line in file if line.strip()]

        self.N_size = len(lines)
        self.grid = []

        for line in lines:
            row = list(line)
            if len(row) < self.N_size:
                row.extend([' '] * (self.N_size - len(row)))
            self.grid.append(row)

    def is_wall(self, x, y):
        if not (0 <= x < self.N_size and 0 <= y < self.N_size):
            return False
        return self.grid[x][y] == 'М'

    def is_exit(self, x, y):
        if self.is_wall(x, y):
            return False
        return x == 0 or x == self.N_size - 1 or y == 0 or y == self.N_size - 1

    def is_free(self, x, y):
        return 0 <= x < self.N_size and 0 <= y < self.N_size and self.grid[x][y] == ' '


class MazeSolver:
    def __init__(self, maze, start_x, start_y):
        self.maze = maze
        self.start_x = start_x
        self.start_y = start_y
        self.best_path = None
        self.best_length = float('inf')

        self.visited = [[False] * maze.N_size for _ in range(maze.N_size)]
        self.steps = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

    def solve(self):
        if self.maze.is_wall(self.start_x, self.start_y):
            return None
        else:
            self.visited[self.start_x][self.start_y] = True
            self._dfs(self.start_x, self.start_y, '', 0)
            return self.best_path

    def _dfs(self, x, y, path, length):
        if length >= self.best_length:
            return

        if self.maze.is_exit(x, y):
            if length < self.best_length:
                self.best_length = length
                self.best_path = path
            return

        for dx, dy, symbol in self.steps:
            nx, ny = x + dx, y + dy

            if self.maze.is_free(nx, ny) and not self.visited[nx][ny]:
                self.visited[nx][ny] = True
                self._dfs(nx, ny, path + symbol, length + 1)
                self.visited[nx][ny] = False


def main():
    maze = Maze('BackTrack.txt')

    while True:
        try:
            start_x = int(input('Введите начальную строку (X): '))-1
            start_y = int(input('Введите начальный столбец (Y): '))-1
            if 0 <= start_x <= maze.N_size - 1 and 0 <= start_y <= maze.N_size - 1:
                break
            else:
                print('Повторите попытку')
        except ValueError:
            print('Повторите попытку')


    solver = MazeSolver(maze, start_x, start_y)
    path = solver.solve()

    if path is None:
        print('\nСтарт не может начинаться в стене!')
    else:
        print(f'\nКратчайший путь: {path}')
        print(f'Длина пути (количество шагов): {len(path)}')


if __name__ == '__main__':
    main()
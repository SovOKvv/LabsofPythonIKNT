# Дано бинарное дерево и корень дерева P1. Необходимо проверить есть ли в
# дереве значение X. В качестве результата вернуть True или False. Решение должно иметь
# сложность по времени исполнения T(n) = O(log n), где n - число вершин в дереве.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return

        curr = self.root
        while True:
            if data < curr.data:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right

    def search(self, x):
        curr = self.root
        while curr:
            if curr.data == x:
                return True
            elif x < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return False


if __name__ == "__main__":

    print('Проверка дерева есть ли в нём число X')
    print('\nВвод из файла TreeWork.txt'
          '\nПервая строка - значения'
          '\nВторая строка - число X')
    tree = BinarySearchTree()

    try:
        with open('TreeWork.txt', 'r') as f:
            line = f.readline()
            if line:
                for value in line.split():
                    tree.insert(int(value))
            x = int(f.readline().strip())

    except FileNotFoundError:
        print('Файл TreeWork.txt не найден')
        exit()

    print(f"\nЕсть ли число {x} в дереве:", tree.search(x))

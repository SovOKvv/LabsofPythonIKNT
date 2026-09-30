# Дано бинарное дерево и корень дерева P1. Необходимо вывести второе
# максимальное значение в дереве. Решение должно иметь сложность по времени исполнения
# T(n) = O(log n), где n - число вершин в дереве.

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

    def find_second_maximum(self):
        if not self.root or (not self.root.left and not self.root.right):
            return 'В дереве недостаточно элементов'

        parent = None
        curr = self.root

        while curr.right:
            parent = curr
            curr = curr.right

        max_node = curr

        if max_node.left:
            curr = max_node.left
            while curr.right:
                curr = curr.right
            return curr.data

        if parent:
            return parent.data

        if self.root == max_node and self.root.left:
            curr = self.root.left
            while curr.right:
                curr = curr.right
            return curr.data

        return 'В дереве недостаточно элементов'


if __name__ == "__main__":
    tree = BinarySearchTree()
    print('Нахождение второго максимума в дереве')
    print('\nВвод из файла TreeWork.txt'
          '\nПервая строка - значения')

    try:
        with open('TreeWork.txt', 'r') as f:
            line = f.readline()
            if line:
                for value in line.split():
                    tree.insert(int(value))

    except FileNotFoundError:
        print('Файл TreeWork.txt не найден')
        exit()

    print('\nВторое максимальное значение:', tree.find_second_maximum())

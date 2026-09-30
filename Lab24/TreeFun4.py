# Реализовать для бинарного дерева интерфейс итератора, который будет возвращать
# значения элементов, находящихся в узлах дерева, в порядке "право-корень-лево".
# Преобразовывать дерево в список или иную структуру данных нельзя, рекурсию использовать
# запрещается.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def build_balanced(self, values):
        sorted_vals = sorted(values)

        def build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = TreeNode(sorted_vals[mid])
            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)
            return node

        self.root = build(0, len(sorted_vals) - 1)

    def print_tree_visual(self, node=None, level=0, prefix="Корень: "):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if not node:
            return

        print("    " * level + prefix + str(node.data))

        if node.left or node.right:
            if node.right:
                self.print_tree_visual(node.right, level + 1, "R-- ")
            else:
                print("    " * (level + 1) + "R-- None")

            if node.left:
                self.print_tree_visual(node.left, level + 1, "L-- ")
            else:
                print("    " * (level + 1) + "L-- None")

    def __iter__(self):
        """
        Итератор в порядке право-корень-лево
        """
        stack = []
        curr = self.root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()
            yield curr.data

            curr = curr.left


if __name__ == "__main__":
    try:
        with open('TreeWork.txt', 'r', encoding='utf-8') as f:
            line = f.readline()
            if line:
                values = [int(v) for v in line.split()]
            else:
                values = []
    except FileNotFoundError:
        print('Файл TreeWork.txt не найден')
        exit()

    print("Исходные данные из файла:", " ".join(map(str, values)))

    tree = BST()
    tree.build_balanced(values)

    print("\nСтруктура получившегося дерева:")
    tree.print_tree_visual()

    print("\nРезультат работы итератора (право-корень-лево):")
    iterator_result = [val for val in tree]
    print(" ".join(map(str, iterator_result)))
# Дано бинарное дерево и корень дерева P1. Необходимо вывести содержимое дерева в возрастающем порядке.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class OrdinaryBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if not curr.left:
                curr.left = new_node
                return
            else:
                queue.append(curr.left)

            if not curr.right:
                curr.right = new_node
                return
            else:
                queue.append(curr.right)

    def print_ascending(self):
        elements = []
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr:
                elements.append(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        elements.sort()
        print('Содержимое дерева по возрастанию:', " ".join(map(str, elements)))

if __name__ == "__main__":
    tree = OrdinaryBinaryTree()

    try:
        with open('TreeWork.txt', 'r') as f:
            line = f.readline()
            if line:
                for value in line.split():
                    tree.insert(int(value))
    except FileNotFoundError:
        print('Файл TreeWork.txt не найден')
        exit()

    tree.print_ascending()
# В первой строке текстового файла записаны целые числа, разделенные
# пробелами. Создать дерево поиска, последовательно включая в него перечисленные в файле
# числа. После этого необходимо, привести дерево к АВЛ-сбалансированному виду, выполнив
# для LR-поворот. Известно, что требуется не более одного такого поворота. Вывести корень
# полученного дерева.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class AVLBalancer:
    def __init__(self, filename_in):
        with open(filename_in, 'r', encoding='utf-8') as f:
            content = f.read().strip()

        if not content:
            self.root = None
            return

        nums = [int(x) for x in content.split()]

        self.root = None
        for num in nums:
            self.root = self.insert(self.root, num)

        self.root = self.apply_lr_rotation(self.root)
        tree_lines = self.print_tree(self.root)

        with open('TreeWork66out.txt', 'w', encoding='utf-8') as f:
            root_val = self.root.value if self.root else "Пусто"
            f.write(f"Корень дерева: {root_val}\n\n")
            f.write("Дерево (на боку):\n")
            f.write('\n'.join(tree_lines) + '\n')

    def insert(self, root, val):
        if not root:
            return Node(val)
        if val < root.value:
            root.left = self.insert(root.left, val)
        elif val > root.value:
            root.right = self.insert(root.right, val)
        return root

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y

    def right_rotate(self, z):
        y = z.left
        T2 = y.right
        y.right = z
        z.left = T2
        return y

    def apply_lr_rotation(self, root):
        return self._find_and_rotate_lr(root)

    def _find_and_rotate_lr(self, node):
        if not node:
            return None

        node.left = self._find_and_rotate_lr(node.left)
        node.right = self._find_and_rotate_lr(node.right)

        balance = self.get_balance(node)


        if balance == 2:
            left_balance = self.get_balance(node.left)
            if left_balance == -1:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        return node

    def print_tree(self, node, level=0):
        if not node:
            return []
        res = self.print_tree(node.right, level + 1)
        res.append(' ' * (level * 4) + f"{node.value:>4}")
        res.extend(self.print_tree(node.left, level + 1))
        return res


balancer = AVLBalancer('TreeWork66.txt')
if balancer.root:
    print(f"Корень полученного дерева: {balancer.root.value}")
else:
    print("Дерево пустое.")
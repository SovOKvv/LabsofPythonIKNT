# Дано дерево поиска и корень дерева P1. Удалить в дереве корневую вершину.
# При замене содержимого удаляемой вершины использовать данные из ее левого поддерева.
# После удаления вывести строку с описанием исходного дерева в следующем формате:
# <дерево>::=((<левое поддерево>)<вершина>(<правое поддерево>)) | ((<левое поддерево>)
# <вершина>) | (<вершина>(<правое поддерево>)) <вершина>::=<цифра><цифра> |
# <цифра> <левое поддерево>::=<дерево> <правое поддерево>::=<дерево> Например,
# "(((1)2((3)4))5(6(7)))". Пробелы в результирующей строке отсутствуют, ссылки на пустые
# деревья никак не выводятся.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeWork26:
    def __init__(self, filename_in, filename_out):
        with open(filename_in, 'r', encoding='utf-8') as f:
            line = f.read().strip()

        root = self.parse_tree(line)
        new_root = self.delete_root(root)
        result_string = self.serialize(new_root)

        with open(filename_out, 'w', encoding='utf-8') as f:
            f.write(result_string + '\n')

    def parse_tree(self, s):
        s = s.strip()
        if not s:
            return None
        if s[0] != '(':
            return Node(int(s))

        inner = s[1:-1]
        left_str, remainder = None, inner

        if inner.startswith('('):
            balance = i = 0
            for i, char in enumerate(inner):
                balance += (char == '(') - (char == ')')
                if balance == 0:
                    i += 1
                    break
            left_str, remainder = inner[:i], inner[i:]

        j = 0
        while j < len(remainder) and remainder[j].isdigit():
            j += 1

        return Node(
            int(remainder[:j]),
            self.parse_tree(left_str) if left_str else None,
            self.parse_tree(remainder[j:]) if remainder[j:] else None
        )

    def delete_root(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return None
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        curr = root.left
        parent = None
        while curr.right:
            parent = curr
            curr = curr.right

        root.value = curr.value

        if parent:
            parent.right = curr.left
        else:
            root.left = curr.left

        return root

    def serialize(self, node):
        if not node:
            return ""
        if not node.left and not node.right:
            return str(node.value)
        if node.left and node.right:
            return f"({self.serialize(node.left)}{node.value}{self.serialize(node.right)})"
        if node.left:
            return f"({self.serialize(node.left)}{node.value})"
        return f"({node.value}{self.serialize(node.right)})"


TreeWork26('TreeWork26.txt', 'TreeWork26out.txt')
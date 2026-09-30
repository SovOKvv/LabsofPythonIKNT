# Дан корень дерева, хранящего арифметическое выражение. В выражении
# участвуют неотрицательные однозначные целые числа, знаки операций кодируются
# отрицательными числами: сложению соответствует -1, вычитанию -2, умножению -3, делению
# -4. Создать копию этого дерева и в созданной копии заменить все выражения вида: 0+a, a+0,
# a-0 на a. Учесть, что в качестве a может быть выражение. Если в результате одного
# преобразования дерева вновь появляются выражения данного вида, их так же нужно
# преобразовывать и в результирующем дереве таких выражений быть не должно. Вывести
# указатель на корень дерева, полученного в результате, и полученное арифметическое
# выражение в виде строки символов.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeWork38:
    def __init__(self, filename_in, filename_out):
        with open(filename_in, 'r', encoding='utf-8') as f:
            line = f.read().strip()

        root = self.parse_tree(line)
        copied_root = self.copy_tree(root)
        optimized_root = self.simplify(copied_root)
        expression_str = self.to_string(optimized_root)

        with open(filename_out, 'w', encoding='utf-8') as f:
            f.write(f"Указатель на корень: {optimized_root}\n")
            f.write(f"Выражение: {expression_str}\n")

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
        if j < len(remainder) and remainder[j] == '-':
            j += 1
        while j < len(remainder) and remainder[j].isdigit():
            j += 1

        root_val = int(remainder[:j])
        right_str = remainder[j:] if j < len(remainder) else None

        return Node(
            root_val,
            self.parse_tree(left_str) if left_str else None,
            self.parse_tree(right_str) if right_str else None
        )

    def copy_tree(self, node):
        if not node:
            return None
        return Node(node.value, self.copy_tree(node.left), self.copy_tree(node.right))

    def is_literal_zero(self, node):
        return node is not None and node.value == 0 and node.left is None and node.right is None

    def simplify_once(self, node):
        if not node:
            return None, False

        node.left, left_changed = self.simplify_once(node.left)
        node.right, right_changed = self.simplify_once(node.right)

        changed = left_changed or right_changed

        if node.value == -1:
            if self.is_literal_zero(node.left):
                return node.right, True
            if self.is_literal_zero(node.right):
                return node.left, True
        elif node.value == -2:
            if self.is_literal_zero(node.right):
                return node.left, True

        return node, changed

    def simplify(self, node):
        while True:
            node, changed = self.simplify_once(node)
            if not changed:
                break
        return node

    def to_string(self, node):
        if not node:
            return ''
        if node.left is None and node.right is None:
            return str(node.value)

        op_map = {-1: '+', -2: '-', -3: '*', -4: '/'}
        op_str = op_map.get(node.value, '?')

        left_str = self.to_string(node.left) if node.left else ''
        right_str = self.to_string(node.right) if node.right else ''

        return f"({left_str}{op_str}{right_str})"


TreeWork38('TreeWork38.txt', 'TreeWork38out.txt')
# В текстовом файле с именем filename дано арифметическое выражение в
# обратной польской записи. Операндами в выражении являются целые числа из промежутка
# от 0 до 9. Используемые операции: сложение (+), вычитание (-), умножение (*) и деление
# нацело (/). Постройте дерево, соответствующее данному выражению. Знаки операций
# кодируйте числами: сложение(-1), вычитание(-2), умножение(-3), деление нацело (-4).
# Преобразуйте дерево так, чтобы в нем не было операции сложения (замените поддеревья, в
# которых есть сложение значением данного поддерева). Выведите указатель на корень
# полученного дерева.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None

    values = content.split()
    if not values and content:
        values = list(content)

    stack = []
    for value in values:
        if value.isdigit():
            stack.append(Node(int(value)))
        else:
            if value == '+':
                op_code = -1
            elif value == '-':
                op_code = -2
            elif value == '*':
                op_code = -3
            elif value == '/':
                op_code = -4
            else:
                continue

            node = Node(op_code)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack[0] if stack else None


def transform(node):
    if node is None:
        return 0, False

    if node.left is None and node.right is None:
        return node.val, False

    left_val, left_has_add = transform(node.left)
    right_val, right_has_add = transform(node.right)

    if node.val == -1:
        current_val = left_val + right_val
    elif node.val == -2:
        current_val = left_val - right_val
    elif node.val == -3:
        current_val = left_val * right_val
    elif node.val == -4:
        current_val = left_val // right_val if right_val != 0 else 0
    else:
        current_val = node.val

    has_add = (node.val == -1) or left_has_add or right_has_add

    if has_add:
        node.val = current_val
        node.left = None
        node.right = None
        return current_val, False

    return current_val, has_add


def transform_tree(root):
    transform(root)
    return root


if __name__ == '__main__':
    root = build_tree('CalcTree2.txt')
    transformed_root = transform_tree(root)

    print(f"Указатель на корень полученного дерева: {transformed_root}")
    print(f"Значение в корне преобразованного дерева: {transformed_root.val if transformed_root else 'Дерево пусто'}")
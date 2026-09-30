# В текстовом файле с именем FN1 дано арифметическое выражение в инфиксной
# форме. В выражении могут использоваться операции: сложение(+), вычитание(-),
# умножение(*), деление нацело(/), остаток от деления(%), возведение в степень(^), а так же
# целые числа из промежутка [1; 30] и переменная x. Для операции возведения в степень
# показатель степени неотрицательное целое число. Постройте дерево выражения. После этого
# вычислите значение выражения при заданном значении переменной x и выведите результат в
# текстовый файл с именем FN2. Преобразуйте дерево, заменив все поддеревья вида x*A на A*x,
# где A - некоторое поддерево, а x - переменная. Распечатайте дерево после преобразования в
# файл FN2 используя многострочный формат, в котором дерево положено на бок. Каждый
# уровень дерева выводите в 4-х позициях и используйте выравнивание по правому краю. При
# наличии нескольких подряд идущих одинаковых операций дерево должно строиться по
# правилу: операции одинакового приоритета вычисляются по порядку слева направо. Иными
# словами, выражение 2+3+4+5, например, должно трактоваться как ((2+3)+4)+5, и не может
# трактоваться как (2+3)+(4+5) или 2+(3+(4+5)). Результаты всех вычислений, включая
# промежуточные, принадлежат типу int.

class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class CalcTree24:
    def __init__(self, filename_in, filename_out, x):
        with open(filename_in, 'r', encoding='utf-8') as f:
            text = f.read()

        self.values = []
        i = 0
        while i < len(text):
            if text[i].isspace():
                i += 1
            elif text[i].isdigit():
                num = ''
                while i < len(text) and text[i].isdigit():
                    num += text[i]
                    i += 1
                self.values.append(num)
            elif text[i] in '+-*/%^()x':
                self.values.append(text[i])
                i += 1
            else:
                i += 1

        self.pos = 0
        root = self.parse_expr()

        res = self.evaluate(root, x)
        root = self.transform(root)
        tree_lines = self.print_tree(root)

        with open(filename_out, 'w', encoding='utf-8') as f:
            f.write(str(res) + '\n' + '\n'.join(tree_lines) + '\n')

    def peek(self):
        return self.values[self.pos] if self.pos < len(self.values) else None

    def consume(self):
        t = self.peek()
        self.pos += 1
        return t

    def parse_expr(self):
        node = self.term()
        while self.peek() in ('+', '-'):
            op = self.consume()
            node = Node(op, node, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.peek() in ('*', '/', '%'):
            op = self.consume()
            node = Node(op, node, self.factor())
        return node

    def factor(self):
        node = self.primary()
        if self.peek() == '^':
            op = self.consume()
            node = Node(op, node, self.factor())
        return node

    def primary(self):
        t = self.consume()
        if t == '(':
            node = self.parse_expr()
            self.consume()
            return node
        return Node(t)

    def evaluate(self, node, x):
        if node.value == 'x': return x
        if node.value.isdigit(): return int(node.value)
        l, r = self.evaluate(node.left, x), self.evaluate(node.right, x)
        if node.value == '+': return l + r
        if node.value == '-': return l - r
        if node.value == '*': return l * r
        if node.value == '/': return int(l / r)
        if node.value == '%': return l % r
        if node.value == '^': return l ** r

    def transform(self, node):
        if not node: return None
        node.left, node.right = self.transform(node.left), self.transform(node.right)
        if node.value == '*' and node.left and node.left.value == 'x':
            node.left, node.right = node.right, node.left
        return node

    def print_tree(self, node, level=0):
        if not node: return []
        res = self.print_tree(node.right, level + 1)
        res.append(' ' * (level * 4) + f"{node.value:>4}")
        res.extend(self.print_tree(node.left, level + 1))
        return res


CalcTree24('CalcTree24.txt', 'CalcTree24out.txt', 4)
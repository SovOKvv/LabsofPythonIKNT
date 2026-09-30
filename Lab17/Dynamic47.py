# Дано число K (> 0) и ссылка A0 на один из элементов непустого двусвязного списка.
# Переместить в списке данный элемент на K позиций назад (если перед данным элементом
# находится менее K элементов, то переместить его в начало списка). Вывести ссылки на
# первый и последний элементы преобразованного списка. Новые объекты типа Node не
# создавать, свойства Data не изменять.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DblLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add_to_end(self, data):
        new_node = Node(data)
        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

    def display(self):
        current = self.first
        while current is not None:
            print(current.data, end='')
            if current.next is not None:
                print(' <-> ', end='')
            current = current.next
        print()

    def node_by_ind(self, index):
        if index < 0:
            return None
        current = self.first
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def update_bounds(self, start_node):
        if start_node is None:
            return

        first = start_node
        while first.prev is not None:
            first = first.prev

        last = start_node
        while last.next is not None:
            last = last.next

        self.first = first
        self.last = last

    def move_back(self, A0, K_steps):
        """Перемещает узел A0 на K_steps позиций назад по двусвязному списку.

            Parameters
            ----------
            A0 : Node
                Ссылка на узел, который необходимо переместить.
            K_steps : int
                Количество позиций для сдвига назад (влево).

        """
        if A0 is None or K_steps <= 0:
            self.update_bounds(A0)
            return

        target = A0
        steps = 0
        while steps < K_steps and target.prev is not None:
            target = target.prev
            steps += 1

        if target == A0:
            self.update_bounds(A0)
            return

        if A0.prev is not None:
            A0.prev.next = A0.next
        if A0.next is not None:
            A0.next.prev = A0.prev

        A0.prev = target.prev
        A0.next = target

        if target.prev is not None:
            target.prev.next = A0
        target.prev = A0

        self.update_bounds(A0)


print('Перемещение элемента на К узлов назад в списке\n')
print('(ввод из файла Dynamic47.txt)')
print('1 строка - К, A0\n2 строка - список\n')

try:
    with open('Dynamic47.txt', 'r') as f:
        K, A0_numb = map(int, f.readline().split())
        values = list(map(int, f.readline().split()))
except FileNotFoundError:
    print('Файл Dynamic47.txt не найден')
    exit()

dllist = DblLinkedList()
for val in values:
    dllist.add_to_end(val)

A0_link = dllist.node_by_ind(A0_numb)

if A0_link is None:
    print(f'Ошибка: Некорректный индекс A0 = {A0_numb}')
else:
    print(f'Исходный список (K = {K}, A0 = {A0_link.data}):')
    dllist.display()
    dllist.move_back(A0_link, K)

    print('\nПреобразованный список:')
    dllist.display()

    print(f'\nСсылка на первый элемент: {dllist.first} (значение: {dllist.first.data})')
    print(f'Ссылка на последний элемент: {dllist.last} (значение: {dllist.last.data})')
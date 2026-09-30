# Даны числа D1 и D2 и ссылка A0 на один из элементов непустого двусвязного списка.
# Добавить в начало списка новый элемент со значением D1, а в конец — новый элемент
# со значением D2. Вывести ссылки на первый и последний элементы полученного списка.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DblLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None

    def add_start(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node

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

    def node_by_ind(self, index):
        current = self.first
        for i in range(index):
            if current is not None:
                current = current.next
        return current

print('Добавление элементов в начало и конец списка\n')
print('(ввод из файла Dynamic32.txt)')
print('1 строка - D1 D2 A0\n2 строка - список\n')

try:
    with open('Dynamic32.txt', 'r') as f:
        D1, D2, A0_numb = map(int, f.readline().split())
        values = list(map(int, f.readline().split()))
except FileNotFoundError:
    print('Файл Dynamic47.txt не найден')
    exit()

dllist = DblLinkedList()
for val in values:
    dllist.add_to_end(val)

A0_link = dllist.node_by_ind(A0_numb)

if A0_link is None:
    print(f'Некорректный индекс A0: {A0_numb}. Узел не найден.')
else:
    first = A0_link
    while first.prev is not None:
        first = first.prev

    last = A0_link
    while last.next is not None:
        last = last.next

    dllist.first = first
    dllist.last = last

    print(f'D1 =  {D1}, D2 = {D2}, A0 = {A0_link}\n')
    print('Исходный список:')
    dllist.display()

    dllist.add_start(D1)
    dllist.add_to_end(D2)

    print('\nИтоговый список:')
    dllist.display()

# Даны ссылки A1, A2 и A3 на первый, последний и текущий элементы двусвязного
# списка (если список является пустым, то A1 = A2 = A3 = null). Также дано число N (> 0) и
# набор из N чисел. Включить в класс IntList (см. задание Dynamic59) процедуру InsertFirst(D),
# которая добавляет новый элемент со значением D в начало списка (D — входной параметр
# целого типа). Добавленный элемент становится текущим. С помощью метода InsertFirst
# добавить в начало исходного списка данный набор чисел (добавленные числа будут
# располагаться в списке в обратном порядке) и вывести ссылки на первый, последний и
# текущий элементы полученного списка.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class IntList:
    def __init__(self, aFirst=None, aLast=None, aCurrent=None):
        self.first = aFirst
        self.last = aLast
        self.current = aCurrent

    def InsertLast(self, D: int):
        new_node = Node(D)
        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

        self.current = new_node

    def InsertFirst(self, D: int):
        new_node = Node(D)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node

        self.current = new_node

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

    def put(self):
        print(f'first: {self.first}, last: {self.last}, current: {self.current}')


try:
    with open('Dynamic60.txt', 'r') as f:
        N, A3_ind = map(int, f.readline().split())
        values_N = list(map(int, f.readline().split()))
        values_List = list(map(int, f.readline().split()))
except FileNotFoundError:
    print('Файл Dynamic60.txt не найден')
    exit()

temp_list = IntList()
for val in values_List:
    temp_list.InsertLast(val)

A1 = temp_list.first
A2 = temp_list.last
A3 = temp_list.node_by_ind(A3_ind)

int_list = IntList(A1, A2, A3)

print('Добавление N чисел в начало списка\n')
print('(ввод из файла Dynamic60.txt)')
print('1 строка - N, A3\n2 строка - список N\n3 строка - исходный список\n')

print('Исходный список:')
int_list.display()

for num in values_N:
    int_list.InsertFirst(num)

print('\nПреобразованный список:')
int_list.display()
print('\nСсылки на элементы:')
int_list.put()

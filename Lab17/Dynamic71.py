# Даны ссылки A1 и A2 на барьерный и текущий элементы двусвязного списка (о
# списке с барьерным элементом см. задание Dynamic70). Разбить список на два, перенеся во
# второй список все элементы от текущего до последнего и добавив ко второму списку
# барьерный элемент. Если текущий элемент исходного списка является барьерным элементом,
# то второй список должен быть пустым (т. е. состоять только из барьерного элемента). Вывести
# ссылку на барьерный элемент второго списка. Не создавать новые объекты типа Node, за
# исключением барьерного элемента для второго списка.

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
        self.prev = None


class CyclicBarrierList:
    def __init__(self):
        self.barrier = Node(0)
        self.barrier.next = self.barrier
        self.barrier.prev = self.barrier

    def add_last(self, data: int):
        new_node = Node(data)
        last = self.barrier.prev

        new_node.next = self.barrier
        new_node.prev = last
        last.next = new_node
        self.barrier.prev = new_node

    def display(self):
        current = self.barrier.next
        if current == self.barrier:
            print('[Пустой список]')
            return

        elements = []
        while current != self.barrier:
            elements.append(str(current.data))
            current = current.next
        print(' -> '.join(elements))

    def node_by_ind(self, index):
        current = self.barrier.next
        i = 0
        while current != self.barrier:
            if i == index:
                return current
            current = current.next
            i += 1
        return self.barrier

    def split_at(self, A2_current):
        """
            Разбивает циклический список с барьерным элементом на два списка.

            Переносит во второй список все элементы, начиная от узла A2_current
            и заканчивая последним узлом текущего списка.

            Parameters
            ----------
            A2_current : Node
                Ссылка на узел, начиная с которого элементы переносятся
                во второй список.

            Returns
            -------
            Node
                Ссылка на новый барьерный элемент второго циклического списка.
        """
        barrier2 = Node(0)


        if A2_current == self.barrier:
            barrier2.next = barrier2
            barrier2.prev = barrier2
            return barrier2


        first2 = A2_current
        last2 = self.barrier.prev
        last1 = A2_current.prev


        self.barrier.prev = last1
        last1.next = self.barrier

        barrier2.next = first2
        first2.prev = barrier2

        last2.next = barrier2
        barrier2.prev = last2

        return barrier2


try:
    with open('Dynamic71.txt', 'r') as f:
        A2_ind = int(f.readline().strip())
        values = list(map(int, f.readline().split()))
except FileNotFoundError:
    print('Файл Dynamic60.txt не найден')
    exit()

list1 = CyclicBarrierList()
for val in values:
    list1.add_last(val)

A1 = list1.barrier
A2 = list1.node_by_ind(A2_ind)

print('Исходный список:')
list1.display()

barrier2_link = list1.split_at(A2)

list2 = CyclicBarrierList()
list2.barrier = barrier2_link

print('\n--- Результаты ---')
print('1-й полученный список (остаток):')
list1.display()

print('2-й полученный список:')
list2.display()

print(f'\nСсылка на барьерный элемент 2-го списка: {barrier2_link}, '
      f'\nЗначение prev: {barrier2_link.prev.data} next: {barrier2_link.next.data}\n')
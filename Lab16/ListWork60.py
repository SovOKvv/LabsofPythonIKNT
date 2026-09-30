# Дан односвязный линейный список и указатель на голову списка P1. Значения
# элементов списка упорядочены по возрастанию. Необходимо создать копию исходного списка,
# после чего во вновь созданном списке вставить в список значение M так, чтобы он остался
# упорядоченным и вывести ссылку на первый элемент полученного списка P2.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "[Пустой список]")

    def copy(self):
        new_list = LinkedList()
        if self.head is None:
            return new_list

        new_list.head = Node(self.head.data)
        current_orig = self.head.next
        current_copy = new_list.head

        while current_orig is not None:
            new_node = Node(current_orig.data)
            current_copy.next = new_node
            current_copy = new_node
            current_orig = current_orig.next

        return new_list

    def insert_sorted(self, M):
        """Создает копию текущего списка, вставляет значение M с сохранением
        порядка возрастания и возвращает (new_list, P2_head).
        """
        new_list = self.copy()
        new_node = Node(M)

        if new_list.head is None or M <= new_list.head.data:
            new_node.next = new_list.head
            new_list.head = new_node
            return new_list, new_list.head

        current = new_list.head
        while current.next is not None and current.next.data < M:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return new_list, new_list.head


list1 = LinkedList()
values = None

while values is None:
    try:
        values = list(map(int, input('Введите числа через пробел: ').split()))
        if len(values) < 2:
            print('Повторите попытку')
            values = None
            continue
    except ValueError:
        print('Повторите попытку')
        values = None

if values:
    list1.head = Node(values[0])
    curr = list1.head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next

P1 = list1.head

M = int(input('Введите число М: '))
list2, P2 = list1.insert_sorted(M)

print(f"\nНовый список после вставки M = {M}:")
list2.display()

print("\nПроверка исходного списка P1:")
list1.display()

print(f"\nСсылка P1 (голова 1-го списка): {P1}")
print(f"Ссылка P2 (голова 2-го списка): {P2}")

# 10 20 30 40 50 60
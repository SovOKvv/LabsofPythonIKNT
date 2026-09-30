# Дан односвязный линейный список и указатель на голову списка P1. Необходимо вывести указатель
# на третий элемент этого списка P3. Известно, что в исходном списке не менее 3 элементов

print('Вывод указателя на третий элемент списка\n')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next

nums = None

while nums is None:
    try:
        nums = list(map(float, input('Введите числа через пробел: ').split()))
        if len(nums) < 2:
            print('Повторите попытку')
            nums = None
            continue
    except ValueError:
        print('Повторите попытку')
        nums = None

new_list = LinkedList()

for num in nums:
    new_list.append(num)

P1 = new_list.head
P3 = new_list.head.next.next

print('Список:')
print(new_list.display())
print('P1 = ', P1)
print('P3 = ', P3)
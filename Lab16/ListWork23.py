# Дан односвязный линейный список и указатель на голову списка P1. Необходимо вставить значение M
# после каждого третьего элемента списка, и вывести ссылку на последний элемент полученного списка P2.

print('Вставка числа каждый 3-ий элемент\n')

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
        print('None')

    def insert_M(self, data):
        """
            Вставляет новый узел со значением data после каждого третьего элемента списка.

            Parameters
            ----------
            data : int
        """
        flag = 1
        current = self.head
        while current:
            if flag % 3 == 0:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node

                current = new_node.next
            else:
                current = current.next

            flag += 1

    def return_tail(self):
        current = self.head
        if self.head is None or self.head.next is None:
            return 'В списке пусто.'

        while current.next is not None:
            current = current.next
        return current

nums, num_M = None, None

while nums is None or num_M is None:
    try:
        nums = list(map(float, input('Введите числа через пробел: ').split()))
        num_M = int(input('Введите M:'))
        if len(nums) < 3:
            print('Повторите попытку')
            nums = None
            continue
    except ValueError:
        print('Повторите попытку')
        nums = None

myList = LinkedList()
for data in nums:
    myList.append(data)

print('Изначальный список:')
myList.display()
P1 = myList.head
print(f'Указатель на голову списка (P1): {P1}\n')
myList.insert_M(num_M)
P2 = myList.return_tail()
print('Измененный список: ')
myList.display()
print(f'Последний элемент списка (P2): {P2}')

# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
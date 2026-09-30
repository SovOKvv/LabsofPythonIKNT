# Дано число N_size (> 0) и набор из N_size чисел. Создать стек, содержащий исходные числа
# (последнее число будет вершиной стека), и вывести ссылку на его вершину

print('Ссылка на вершину стека\n')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.isempty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def get_head(self):
        return self.head

    def get_head_data(self):
        if self.isempty():
            return None
        return self.head.data


while True:
    try:
        count_numb = int(input('Введите количество чисел: '))
        if count_numb > 0:
            break
        else:
            print('Значение должно быть больше 0')
    except ValueError:
        print('Повторите попытку')

stack = Stack()
print(f'Введите {count_numb} чисел:')
for i in range(count_numb):
    numb = int(input(f'Число {i + 1}: '))
    stack.push(numb)

print(f'\nСсылка на вершину: {stack.get_head()}')
print(f'Данные вершины: {stack.get_head_data()}')

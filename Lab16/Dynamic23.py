# Даны две непустые очереди; начало и конец первой равны A1 и A2, а второй — A3 и A4. Перемещать
# элементы из начала первой очереди в конец второй, пока значение начального элемента первой очереди
# не станет четным (если первая очередь не содержит четных элементов, то переместить из первой очереди
# во вторую все элементы). Вывести новые ссылки на начало и конец первой, а затем второй очереди (для
# пустой очереди дважды вывести null). Новые объекты типа Node не создавать.

print('Перемещение элементов до четного элемента')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isempty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def display(self):
        if self.isempty():
            return 'Очередь пуста'
        elements= []
        now_current = self.head
        while now_current:
            elements.append(str(now_current.data))
            now_current = now_current.next
        return ' '.join(elements)

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def parity(self):
        now_current = self.head
        while now_current:
            if now_current.data % 2 != 0:
                return True
            now_current = now_current.next
        return False

    def transfer(self, queue2):
        """
            Переносит элементы из текущей очереди (self) во вторую очередь (queue2).

            Parameters
            ----------
            queue2 : Queue
                Вторая очередь, в конец которой будут добавлены переносимые элементы.

            Returns
            -------
            tuple[Queue, Queue] | None
                Кортеж из двух очередей (self, queue2) с обновлёнными связями.
        """
        if self.isempty():
            return self, queue2
        if not self.parity():
            if queue2.isempty():
                queue2.head = self.head
                queue2.tail = self.tail
            else:
                queue2.tail.next = self.head
                queue2.tail = self.tail

            self.head = None
            self.tail = None
        else:
            prev = None
            now_current = self.head

            while now_current and now_current.data % 2 != 0:
                prev = now_current
                now_current = now_current.next

            if prev is None:
                return None
            else:
                first_head = self.head
                first_tail = prev

                self.head = now_current
                prev.next = None

                if queue2.isempty():
                    queue2.head = first_head
                    queue2.tail = first_tail
                else:
                    queue2.tail.next = first_head
                    queue2.tail = first_tail
        return self, queue2

with open('Dynamic23.txt', 'r', encoding='utf-8') as file:
    first_line = list(map(int, file.readline().strip().split()))
    second_line = list(map(int, file.readline().strip().split()))

queue1 = Queue()
for num in first_line:
    queue1.enqueue(num)

queue2 = Queue()
for num in second_line:
    queue2.enqueue(num)

print(f'\nНачальное содержимое:')
print('Содержимое первой очереди:', queue1.display())
print('Содержимое второй очереди:', queue2.display())
print(f'head1 = {queue1.head}, tail1 = {queue1.tail}')
print(f'head2 = {queue2.head}, tail2 = {queue2.tail}')

queue1.transfer(queue2)

if queue1.isempty():
    print('\nРезультат:')
    print('Содержимое первой очереди:', queue1.display())
    print('Содержимое второй очереди:', queue2.display())
    print('head1 =  null, tail1 = null')
    print(f'head2 = {queue2.get_head()}, tail2 = {queue2.get_tail()}')
else:
    print('\nРезультат:')
    print('Содержимое первой очереди:', queue1.display())
    print('Содержимое второй очереди:', queue2.display())
    print(f'head1 = {queue1.head}, tail1 = {queue1.tail}')
    print(f'head2 = {queue2.head}, tail2 = {queue2.tail}')
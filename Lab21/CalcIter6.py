# Расширить класс двусвязного циклического списка с барьерным элементом из
# лабораторной работы №16 интерфейсом итератора. Итератор должен возвращать все
# элементы списка в обратном порядке без остановки. Вместо значения барьерного элемента
# итератор должен возвращать строку «barrier».

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
    self.iter_current = self.barrier
    self.returned_barrier = False

  def __iter__(self):
    self.iter_current = self.barrier
    self.returned_barrier = False
    return self

  def __next__(self):
    self.iter_current = self.iter_current.prev

    if self.iter_current == self.barrier:
      if not self.returned_barrier:
        self.returned_barrier = True
        return 'barrier'
      else:
        raise StopIteration

    return self.iter_current.data

  def add_last(self, data):
    new_node = Node(data)
    last = self.barrier.prev

    new_node.next = self.barrier
    new_node.prev = last
    last.next = new_node
    self.barrier.prev = new_node

  def display(self):
    current = self.barrier.next
    if current == self.barrier:
      print('Пустой список')
      return

    elements = []
    while current != self.barrier:
      elements.append(str(current.data))
      current = current.next
    print(' <-> '.join(elements))

try:
    with open('CalcIter6.txt', 'r') as f:
        values = list(map(int, f.readline().split()))
except FileNotFoundError:
    print('Файл CalcIter6.txt не найден')
    exit()

my_list = CyclicBarrierList()

for val in values:
  my_list.add_last(val)

print('Исходный список:')
my_list.display()

print('\nВывод в обратном порядке:')
result_str = ' <-> '.join(map(str, my_list))
print(result_str)
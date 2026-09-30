# Преобразовать двусвязный список в бинарное дерево поиска без использования
# дополнительной памяти (создания новых объектов). Корнем дерева должен стать элемент
# списка, находящийся в его середине, а само дерево должно иметь наименьшую возможную
# высоту. При преобразовании поля left и right узлов бинарного дерева рассматриваются
# эквивалентными полям prev и next узлов двусвязного списка. Вывести исходный список и
# получившееся дерево.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedListToBST:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get_length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def list_to_bst(self):
        n = self.get_length()
        if n == 0:
            return None

        self.current_node = self.head

        def build_tree(start, end):
            if start > end:
                return None

            mid = (start + end) // 2

            left_child = build_tree(start, mid - 1)

            root = self.current_node
            root.prev = left_child

            self.current_node = self.current_node.next
            root.next = build_tree(mid + 1, end)

            return root

        self.head = build_tree(0, n - 1)


    def print_tree_visual(self, node=None, level=0, prefix="Корень: "):
        if node is None:
            if level == 0:
                node = self.head
            else:
                return

        if not node:
            return

        print("    " * level + prefix + str(node.data))

        if node.prev or node.next:
            if node.prev:
                self.print_tree_visual(node.prev, level + 1, "L-- ")
            else:
                print("    " * (level + 1) + "L-- None")

            if node.next:
                self.print_tree_visual(node.next, level + 1, "R-- ")
            else:
                print("    " * (level + 1) + "R-- None")


if __name__ == "__main__":
    dll = DoublyLinkedListToBST()

    try:
        with open('TreeWork.txt', 'r') as f:
            line = f.readline()
            line = sorted(map(int, line.split()))
            if line:
                for value in line:
                    dll.append(int(value))

    except FileNotFoundError:
        print('Файл TreeWork.txt не найден')
        exit()

    dll.list_to_bst()
    print('Получившееся дерево:')
    dll.print_tree_visual()
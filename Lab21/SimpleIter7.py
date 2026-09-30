# Написать класс, реализующий интерфейс итератора. Класс должен принимать в
# конструкторе список элементов произвольного типа и позволять просмотреть его в
# следующем порядке: последний — первый — предпоследний — второй — …

class SimpleIter7:

    def __init__(self, elements):
        self.elements = elements
        self.sequence = []

        left = 0
        right = len(elements) - 1
        while left <= right:
            self.sequence.append(elements[right])
            if left != right:
                self.sequence.append(elements[left])
            left += 1
            right -= 1

        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        result = self.sequence[self.index]
        self.index += 1
        return result


print('Введите элементы списка через пробел:')
user_input = input().strip()

if not user_input:
    print('Список пуст. Нет элементов для обработки.')
else:
    user_elements = user_input.split()

    print(f"\nИсходный список: {' '.join(map(str, user_elements))}")

    iterator = SimpleIter7(user_elements)
    result_str = " ".join(map(str, iterator))
    print(f"Результат обхода: {result_str}")

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
import math

class HuffmanNode:

    def __init__(self, char: str = None, freq: int = 0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoder:

    def __init__(self, text: str):
        if not text:
            raise ValueError('Текст не должен быть пустым')
        self.text = text
        self.codes = {}
        self._build_tree()

    def _count_frequencies(self):
        freqs = {}
        for char in self.text:
            freqs[char] = freqs.get(char, 0) + 1
        return freqs

    def _build_tree(self):
        frequencies = self._count_frequencies()
        nodes = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
        if len(nodes) == 1:
            node = nodes[0]
            self.codes[node.char] = '0'
            return
        while len(nodes) > 1:
            nodes.sort()
            left = nodes.pop(0)
            right = nodes.pop(0)
            parent = HuffmanNode(freq=left.freq + right.freq)
            parent.left = left
            parent.right = right
            nodes.append(parent)
        root = nodes[0]
        self._generate_codes(root, '')

    def _generate_codes(self, node: HuffmanNode, current_code: str):
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code
            return
        self._generate_codes(node.left, current_code + '0')
        self._generate_codes(node.right, current_code + '1')

    def get_codes(self):
        return self.codes

    def get_uniform_size(self):
        unique_chars = len(self._count_frequencies())
        bits_per_char = max(1, math.ceil(math.log2(unique_chars)))
        return len(self.text) * bits_per_char

    def get_huffman_size(self):
        return sum(len(self.codes[char]) for char in self.text)



if __name__ == '__main__':
    text = 'ТЕРРИТОРИЯ ТЕРРАРИУМА'
    try:
        huffman = HuffmanCoder(text)
        print(f'Исходный текст: {text}')
        print('Коды символов:')
        for char, code in sorted(huffman.get_codes().items()):
            char_display = f'\'{char}\'' if char != ' ' else '\' \''
            print(f'  {char_display}: {code}')
        uniform = huffman.get_uniform_size()
        compressed = huffman.get_huffman_size()
        print(f'Размер при равномерном кодировании: {uniform} бит')
        print(f'Размер при кодировании Хаффмана: {compressed} бит')
    except ValueError as e:
        print(f'Ошибка: {e}')
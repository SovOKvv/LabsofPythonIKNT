# Имеется набор сообщений. Для данного сообщения написать программу с кодом Хемминга,который позволит
# обнаруживать одиночную ошибку и исправлять ее. Для проверки привести решение «вручную»,
# в котором виден процесс построения кодов.

class HammingCode:
    """
    Attributes:
        data (list): Исходные данные в виде списка битов (0 и 1)
        data_len (int): Количество информационных битов
        numb_len (int): Количество контрольных битов (r)
        len (int): Общая длина закодированного слова (n = k + r)
        positions (list): Позиции контрольных битов (степени двойки: 1, 2, 4, 8...)
    """
    def __init__(self, data):
        self.data = data
        self.data_len = len(data)

        self.numb_len = 1
        while 2 ** self.numb_len < self.data_len + self.numb_len + 1:
            self.numb_len += 1

        self.len = self.data_len + self.numb_len
        self.positions = [1, 2, 4, 8]

    def encode(self):
        """
        Кодирование исходного сообщения кодом Хэмминга.

        Returns:
           list: Закодированное кодовое слово длиной self.len,
                 где информационные и контрольные биты чередуются согласно
                 правилам кода Хэмминга
        """
        code = [0] * self.len
        num_data = 0
        for i in range(1, self.len + 1):
            if i not in self.positions:
                code[i-1] = self.data[num_data]
                num_data += 1

        for p in self.positions:
            pois_sum = 0
            for i in range(1, self.len + 1):
                if i != p and (i & p):
                    pois_sum = pois_sum ^ code[i-1]
            code[p - 1] = pois_sum

        return code

    def correct(self, received):
        """
        Обнаружение и исправление одиночной ошибки в принятом слове.

        Args:
            received (list): Принятое кодовое слово (может содержать ошибку)

        Returns:
            list: Восстановленное исходное сообщение (информационные биты)

        """
        err = 0
        for p in self.positions:
            bit_sum = 0
            for i in range(1, self.len + 1):
                if i & p:
                    bit_sum ^= received[i - 1]
            if bit_sum:
                err |= p

        if err:
            received[err - 1] ^= 1

        data = []
        for i in range(1, self.len + 1):
            if i not in self.positions:
                data.append(received[i - 1])

        return data

print('Кодирование сообщения кодом Хэмминга\nС нахождением и исправлением 1-ой ошибки')
print('(ввод осуществляется из текстового файла)\n')

with open('ForHammingCode.txt','r') as f:
    bits_str = f.readline().strip()
    message = [int(bit) for bit in bits_str]
    err_num = int(f.readline().strip())

hamming = HammingCode(message)

encoded = hamming.encode()
print("Закодированное:", *encoded)

received = encoded.copy()
received[err_num - 1] = received[err_num - 1] ^ 1
print("С ошибкой:     ", *received)

restored = hamming.correct(received)
print("Восстановлено: ", *restored)
print("Исходное:      ", *message)

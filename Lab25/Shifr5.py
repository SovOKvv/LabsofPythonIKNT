# Написать программу для шифрования и дешифрования последовательности символов шифром A1Z26.

class A1Z26_RUS:
    """
    Шифр A1Z26 для русского алфавита.

    Заменяет каждую букву её порядковым номером в алфавите (А=1, Б=2, ..., Я=33).
    """
    def __init__(self):
        self.alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    def encode(self, text):
        """
        Шифрует текст в числа.

            Args:
                text (str): Исходный текст заглавными буквами.

            Returns:
                str: Закодированная строка, где буквы заменены числами, разделёнными символом '/'.
        """
        result = []

        for i in text:
            if i in self.alphabet:
                num = self.alphabet.index(i) + 1
                result.append(str(num))
            else:
                result.append(i)

        return '/'.join(result)

    def decode(self, encoded):
        """
        Расшифровывает числа в текст.

            Args:
                encoded (str): Закодированная строка с числами, разделёнными символом '/'.

            Returns:
                str: Расшифрованный текст.
        """
        result = []

        for i in encoded.split('/'):
            if i.isdigit():
                num = int(i) - 1
                if 0 <= num < len(self.alphabet):
                    result.append(self.alphabet[num])
                else:
                    result.append(i)
            else:
                result.append(i)

        return ''.join(result)

print('Шифр A1Z26 для русского языка\n')
print('1. Шифрование\n2. Дешифрование\n')

while True:
    version = str(input('Введите число: '))

    if version == '1':
        print('\n(для корректной работы программы вводите только заглавные буквы)')
        text = str(input('Введите сообщение: '))
        code = A1Z26_RUS()
        encoded = code.encode(text)
        print('\nРезультат:', encoded)
        break
    elif version == '2':
        print('\n(вводите числа через /)')
        numbers = str(input('Введите числа: '))
        code = A1Z26_RUS()
        decoded = code.decode(numbers)
        print('\nРезультат:', decoded)
        break
    else:
        print('\n(введите 1 или 2)')

# Пример: СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК, ДА ВЫПЕЙ ЖЕ ЧАЮ
# 19/28/6/26/30/ /6/27/7/ /31/20/10/Damir23/ /14/33/4/12/10/Damir23/ /22/18/1/15/24/21/9/19/12/10/Damir23/ /2/21/13/16/12/,/ /5/1/ /3/29/17/6/11/ /8/6/ /25/1/32
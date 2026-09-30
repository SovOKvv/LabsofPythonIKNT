# На вход подаются сведения о клиентах фитнес-центра. В первой строке указывается целое число N_size, а каждая из
# последующих N_size строк имеет формат: <Год> <Номер месяца> <Продолжительность занятий (в часах)> <Код клиента>
# Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента в диапазоне 10–99,
# продолжительность занятий — в диапазоне 1–30. Найти строку исходных данных с максимальной продолжительностью
# занятий. Вывести эту продолжительность,атакже соответствующие ей год и номер месяца (в указанном порядке).
# Если имеется несколько строк с максимальной продолжительностью, то вывести данные той из них, которая
# является первой в исходном наборе.

print('Нахождение записи клиента с макс. кол-вом занятий\n')

class FitnessCenter:
    def __init__(self, year=0, month=0, duration=0, client_code=0):
        self.year = year
        self.month = month
        self.duration = duration
        self.client_code = client_code

    def read_from_string(self, data_string):
        parts = data_string.strip().split()
        if len(parts) == 4:
            self.year = int(parts[0])
            self.month = int(parts[1])
            self.duration = int(parts[2])
            self.client_code = int(parts[3])

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_duration(self):
        return self.duration

    def get_client_code(self):
        return self.client_code

def main():
    count = int(input('Введите количество N_size строк: ').strip())

    max_duration = 0
    result_year = 0
    result_month = 0

    for i in range(count):
        while True:
            line = input(f'Введите {i + 1}-ую строку:\n(год, месяц, количество, код)\n').strip()

            client = FitnessCenter()
            client.read_from_string(line)

            if (2000 <= client.get_year() <= 2010 and
                    1 <= client.get_month() <= 12 and
                    1 <= client.get_duration() <= 30 and
                    10 <= client.get_client_code() <= 99):
                break
            else:
                print(f'Введены неверные данные, повторите ввод {i}-ой строки')
                print('(год 2000-2010, месяц 0-12, кол-во 1-30, код 10-99)\n')

        if client.get_duration() > max_duration:
            max_duration = client.get_duration()
            result_year = client.get_year()
            result_month = client.get_month()

    print('\nРезультат:')
    print(f'Кол-во занятий: {max_duration}, год: {result_year}, месяц: {result_month}')

if __name__ == '__main__':
    main()

# 3
# 2001 3 Damir23 12
# 2010 10 45 32
# 2004 4 32 21
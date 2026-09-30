# На вход подаются сведения о клиентах фитнес-центра. В первой строке указывается код K одного
# из клиентов, во второй строке —целое число N_size, а каждаяизпоследующих N_size строк имеет формат
# <Год> <Номер месяца> <Код клиента> <Продолжительность занятий (в часах)> Все данные целочисленные.
# Значение года лежит в диапазоне от 2000 до 2010, код клиента в диапазоне 10–99, продолжительность
# занятий — в диапазоне 1–30. Для каждого года,в котором клиент с кодом K посещал центр, определить
# месяц, в котором продолжительность занятий данного клиента была наименьшей для данного года
# (если таких месяцев несколько,то выбирать месяц с наибольшим номером; месяцы с нулевой продолжительностью
# занятий не учитывать). Сведения о каждом годе выводить на новой строке в следующем порядке: год,номер
# месяца, продолжительность занятий в этом месяце. Упорядочивать сведения по возрастанию номера года.
# Если данные о клиенте с кодом K отсутствуют, то вывести строку «Нет данных».

print('Нахождение месяца с мин. продолжительностью за год определенного клиента\n')

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
    while True:
        k_client = int(input('Введите код K клиента: '))
        if 10 <= k_client <= 99:
            break
    count = int(input('Введите количество N_size строк: ').strip())
    print('\n')

    client_data = {}

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

        if client.get_client_code() == k_client:
            year = client.get_year()
            month = client.get_month()
            duration = client.get_duration()

            if year not in client_data:
                client_data[year] = {}
            client_data[year][month] = duration

    if not client_data:
        print('\nНет данных')
    else:
        print(f'\nРезультаты для клиента с кодом {k_client}: ')

        for year in sorted(client_data.keys()):
            all_months = client_data[year]

            if all_months:
                min_duration = min(all_months.values())

                min_months = [month for month, duration in all_months.items()
                              if duration == min_duration]

                result_month = max(min_months)

                print(f"Год: {year}, месяц: {result_month}, продолжительность занятий: {min_duration}")

if __name__ == '__main__':
    main()

# 12
# 5
# 2002 5 12 12
# 2002 8 12 12
# 2009 2 30 12
# 2009 2 15 12
# 2009 2 10 10
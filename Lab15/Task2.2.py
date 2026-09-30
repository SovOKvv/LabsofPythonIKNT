# Имеется информация об учениках младшей школы. Для всех учеников известны: фамилия, имя и класс. Для учеников
# 1-х классов дополнительно известна их скорость чтения (слов в минуту, тип int). Для учеников 4-х классов
# известны баллы итоговой аттестации (единый муниципальный тест от 1 до 100 баллов, тип float). Для учеников
# 2-х и 3-х классов известны данные итоговой школьной контрольной по математике (оценки от 1 до 10 баллов,
# тип float). Написать функцию, позволяющую ввести с клавиатуры данные для одного ученика. Используя эту функцию,
# ввести сведения об N_size учениках и сохранить их в бинарном файле. Распечатать на экране содержимое данного файла
# в виде таблицы.
import pickle

class Student:
    def __init__(self, surname, name, grade):
        self.surname = surname
        self.name = name
        self.grade = grade

    def __str__(self):
        return f'{self.surname:<15} {self.name:<15} {self.grade:<5}'

class FirstStudent(Student):
    def __init__(self, surname, name, grade, read_speed):
        super().__init__(surname, name, grade)
        self.read_speed = read_speed
    def __str__(self):
        return super().__str__() + f'{self.read_speed:<15} {"-":<15} {"-":<15}'

class SecondThirdStudent(Student):
    def __init__(self, surname, name, grade, math_score):
        super().__init__(surname, name, grade)
        self.math_score = math_score
    def __str__(self):
        return super().__str__() + f'{"-":<15} {self.math_score:<15} {"-":<15}'

class FourthStudent(Student):
    def __init__(self, surname, name, grade, test_score):
        super().__init__(surname, name, grade)
        self.test_score = test_score
    def __str__(self):
        return super().__str__() + f'{"-":<15} {"-":<15} {self.test_score:<15}'


def input_student():
    print('\nВведите данные ученика: ')
    surname = input('Фамилия: ')
    name = input('Имя: ')

    while True:
        try:
            grade = int(input('Класс (1-4): '))
            if 1 <= grade <= 4:
                break
            else:
                print('Класс должен быть от 1 до 4')
        except ValueError:
            print('Введите целое число')

    if grade == 1:
        while True:
            try:
                reading_speed = int(input('Скорость чтения: '))
                break
            except ValueError:
                print('Введите целое число')
        return FirstStudent(surname, name, grade, reading_speed)

    elif grade in [2, 3]:
        while True:
            try:
                math_score = float(input('Оценка за контрольную по математике (1-10): '))
                if 1 <= math_score <= 10:
                    break
                else:
                    print('Оценка должна быть от 1 до 10')
            except ValueError:
                print('Повторите попытку')
        return SecondThirdStudent(surname, name, grade, math_score)

    else:
        while True:
            try:
                test_score = float(input('Баллы итоговой аттестации (1-100): '))
                if 1 <= test_score <= 100:
                    break
                else:
                    print('Баллы должны быть от 1 до 100')
            except ValueError:
                print('Повторите попытку')
        return FourthStudent(surname, name, grade, test_score)


def save_students_to_file(students, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump(students, file)
        print(f'\nДанные сохранены в файл {filename}')
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def load_students_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f'Файл {filename} не найден. Будет создан новый список.')
        return []
    except Exception as e:
        print(f'Ошибка при чтении файла: {e}')
        return []

def print_students_table(students):
    if not students:
        print('Нет данных для отображения')
        return

    print(f"\n{'Фамилия':<15} {'Имя':<13} {'Класс':<5} {'Скорость':<15} "
          f"{'Оценка':<15} {'Баллы атт':<15}")
    print('=' * 80)

    for student in students:
        print(student)
    print('=' * 80)

def main():
    filename = 'students.bin'
    students = load_students_from_file(filename)

    while True:
        print('\nМЕНЮ:')
        print('1. Добавить ученика')
        print('2. Сохранить данные в файл')
        print('3. Вывести таблицу учеников')
        print('4. Выйти')

        choice = input('Выберите действие: ')

        if choice == '1':
            student = input_student()
            students.append(student)
            print('Ученик добавлен')

        elif choice == '2':
            save_students_to_file(students, filename)

        elif choice == '3':
            print_students_table(students)

        elif choice == '4':
            break

        else:
            print('Выберите пункт 1-4.')

if __name__ == '__main__':
    print('Ввод инф-ии об учениках, сохранение в бин. файле и вывод в виде таблицы')
    main()

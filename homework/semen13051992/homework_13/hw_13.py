import os
import datetime

base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_file_path)

with open(eugene_file_path, encoding='utf-8') as eugene_file:
    print(eugene_file.read())


def read_file():
    with open(eugene_file_path, encoding='utf-8') as file:
        for line in file:
            yield line


'''
# после создания data2.txt закоментировал, постоянно бобовляет записи в файл после запуска

for line in read_file():
    with open('data2.txt', 'a', encoding='utf-8') as new_file:
        line = line[:29]
        new_file.write(line)
        new_file.write('\n')
'''


def open_data2():
    with open('data2.txt', 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def converting_python_date(date_line):
    python_date = datetime.datetime.strptime(date_line, '%Y-%m-%d %H:%M:%S.%f')
    return python_date


def python_date():
    for line in open_data2():
        if '1.' in line:
            date_line = line.replace('1. ', '')
            date = converting_python_date(date_line)
            date_1 = date + datetime.timedelta(weeks=1)
            print(f'Дата на неделю позже {date_1}')
        elif '2.' in line:
            date_line = line.replace('2. ', '')
            date = converting_python_date(date_line)
            date_2 = str(date.isoweekday()) + ' ' + str(date.strftime('%A'))
            print(f'День недели {date_2}')
        elif '3.' in line:
            date_line = line.replace('3. ', '')
            date = converting_python_date(date_line)
            now = datetime.datetime.now()
            date_3 = now - date
            print(f'{date_3.days} дней назад была эта дата')


python_date()

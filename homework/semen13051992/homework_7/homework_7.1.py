number = 2

while True:
    numbers = int(input('Угадайте цифру: '))
    if number == numbers:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова!')


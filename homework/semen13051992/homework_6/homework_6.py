text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

# print(text.split())

a = 'ing'

new_text = []

for i in text.split():
    if ',' in i:
        i = i.replace(',', '')
        new_text.append(i + a + ',')
    elif  '.' in i:
        i = i.replace('.', '')
        new_text.append(i + a + '.')
    else:
        new_text.append(i + a)

# print(new_text)
print(' '.join(new_text))

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

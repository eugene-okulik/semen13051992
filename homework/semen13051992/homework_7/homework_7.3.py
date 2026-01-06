a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'

def new(text):
    new_text = text.split()
    return int(new_text[-1]) + 10

print(new(a))
print(new(b))
print(new(c))
print(new(d))

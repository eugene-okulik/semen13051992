person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name)
print(last_name)
print(city)
print(phone)
print(country)

a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'

#text_1 = a.split()
#print(text_1)
#print(text_1[-1])
print(a.index(':'))
text_1 = (a[a.index(':') + 1:])
print(text_1)
text_1 = text_1.strip()
print(text_1)
print(type(text_1))
print(int(text_1) + 10)

#text_2 = b.split()
#print(text_2)
#print(text_2[-1])
print(b.index(':'))
text_2 = (b[b.index(':') + 1:])
print(text_2)
text_2 = text_2.strip()
print(text_2)
print(type(text_2))
print(int(text_2) + 10)

#text_3 = c.split()
#print(text_2)
#print(text_3[-1])
print(c.index(':'))
text_3 = (c[c.index(':') + 1:])
print(text_3)
text_3 = text_3.strip()
print(text_3)
print(type(text_3))
print(int(text_3) + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print('Student', ', ' .join(students), 'study these', 'subjects:', ', '.join(subjects))

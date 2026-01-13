PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_text = PRICE_LIST.split()
print(new_text)
new_list = list(map(lambda x: x.replace('р', '') if '0р' in x else x, new_text))
print(new_list)

list_int = list(map(int, new_list[1::2]))
print(list_int)
list_str = list(map(str, new_list[0::2]))
print(list_str)

new_list2 = dict(zip(list_str, list_int))
print(new_list2)

my_dict = {
    'tuple' : (1, 2.2, False, 'text2', 8),
    'list' : [1.4, 2, True, 'text', 5],
    'dict' : {'one' : 'value',
              'two' : 'value2',
              'three' : 'value3',
              'four' : 'value4',
              'five' : 'value5'},
    'set' : {1, 'twoo', 3, False, 2.45}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('text3')
my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict']['i am a tuple'] = 'text3473'
my_dict['dict'].pop('one')
print(my_dict['dict'])

my_dict['set'].add(34)
my_dict['set'].pop()
print(my_dict['set'])

print(my_dict)

my_dict = {'Nika': 2003, 'Misha': 1994, 'Din': 1979, 'Sam': 1982}
print(my_dict)
print(my_dict['Nika'])
print(my_dict.get('Kas'))
my_dict.update({'Dasha': 1993,
                'Tanya': 1997})
print(my_dict.pop('Nika'))
print(my_dict)


my_set = {8,4,3,0,4,0,0, 'Rima', 'Stas'}
print(my_set)
my_set.add(9)
my_set.add('Oksana')
my_set.remove(3)
print(my_set)
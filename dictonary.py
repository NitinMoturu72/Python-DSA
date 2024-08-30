my_dict = dict()
print(my_dict)
my_dict2 = {}
print(my_dict2)

eng_sp = dict(one = 'uno', two = 'dos', three = 'tres')
print(eng_sp)

eng_sp2 = {'one': 'uno', 'two' : 'dos', 'three' : 'tres'}
print(eng_sp2)

eng_sp_list = [('one' , 'uno'), ('two' , 'dos'), ('three' , 'tres')]
eng_sp3 = dict(eng_sp_list)
print(eng_sp3)


print('Insert/Update elements of Dictionary')

my_dict3 = {'name':'Edy', 'age': 26}
my_dict3['age'] = 27
print(my_dict3)

my_dict3['address'] = 'London'
print(my_dict3)
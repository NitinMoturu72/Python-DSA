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

print('Traversing through Dictionary')

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])
    
traverseDict(my_dict3)

print('Searching an element in Dictionary')

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'

print(searchDict(my_dict3, 27))

print('Deleting an element from a dictionary')

del my_dict3['age']
print(my_dict3)


removed_element = my_dict3.pop('address')
print(removed_element)
print(my_dict3)

print(eng_sp)
print(eng_sp.popitem())
print(eng_sp)


print(eng_sp2)
eng_sp2.clear()
print(eng_sp2)
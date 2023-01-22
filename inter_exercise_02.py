##https://www.w3schools.com/python/python_dictionaries_loop.asp
#found you can loop by keys and can check keys in both this way

def get_combined_dict(dict1, dict2):
    dictComb = dict()
    for key in dict1:
        if key in dict2:
            dictComb.update({key: (dict1[key] + dict2[key])})
    return dictComb

my_dict_1 = {'a': 5, 'b': 15, 'c': 3, 'd': 11}
my_dict_2 = {'b': 5, 'c': 7, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
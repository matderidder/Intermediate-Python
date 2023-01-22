def get_unique_list(user_list):
    unique_list = list()
    for val in user_list:
        if  val not in unique_list:
            unique_list.append(val)
    return unique_list

my_list = [1, 2, 3, 2, 1, 4, 5, 5, 6]
unique_list = get_unique_list(my_list)
print(unique_list)

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_index = 0

while my_list_index != len(my_list):
    list_number = my_list[my_list_index]
    my_list_index = my_list_index + 1
    if list_number < 0:
        break
    elif list_number == 0:
        continue
    else:
        print(list_number)
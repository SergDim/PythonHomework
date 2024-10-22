
def get_multiplied_digits(number):
    str_number = str(number)
    fist = int(str_number[0])
    if len(str_number) > 1:
        return fist * get_multiplied_digits(int(str_number[1:]))
    else:
        return fist

result = get_multiplied_digits(40203)
print(result)
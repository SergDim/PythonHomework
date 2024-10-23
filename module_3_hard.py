
def calculate_structure_sum(*arg):
    sum_arg = 0
    for element in arg:
        if isinstance(element, int):
            sum_arg += element
        elif isinstance(element, str):
            sum_arg += len(element)
        elif isinstance(element, (list, tuple, set)):
            sum_arg += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            sum_arg += calculate_structure_sum(*element.items())
    return sum_arg


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
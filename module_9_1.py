

def apply_all_func(int_list, *functions):
    results = dict()
    for f in functions:
        results.update({f.__name__ : f(int_list)})
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
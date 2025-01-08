

def is_prime(func):
    print("Decorator call")
    def wrapper(*args):
        print("Wrapper call")
        is_simple = True
        res = func(*args)
        for n in range(2, res):
            if res % n == 0:
                is_simple = False
                break
        if is_simple:
            print("Простое")
        else:
            print("Составное")
        return res
    return wrapper

@is_prime
def sum_three(f, s, t):
    return f + s + t

result = sum_three(2, 3, 6)
print(result)

print("Далее вызов декоратора")

func_decor = is_prime(sum_three)
result = func_decor(2, 3, 6)
print(result)


def my_func():
    print("Myfync call.")

my = my_func
my()
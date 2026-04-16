def result(func):
    def wrapper(arg):
        result = func(arg)
        print(f"Результат: {result}")
        return result
    return wrapper

@result
def div_2(num):
    return num // 2

div_2(46)

def operation(func):


    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func

    return wrapper

@operation
def calc(first, second):
    if first == second:
        print(first + second)
        return first + second
    elif first > second:
        print(first - second)
        return first - second
    elif first < second:
        print(second / first)
        return first / second
    elif first < 0 or second < 0:
        print(first * second)
        return first * second


print(calc(3,3))
print(calc(3,2))
print(calc(2,3))
print(calc(-2,3))

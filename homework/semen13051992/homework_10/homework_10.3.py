def operation(func):

    def wrapper(first, second, *args, **kwargs):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')
    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(3, 3))
print(calc(3, 2))
print(calc(2, 3))
print(calc(-2, 3))
print(calc(2, -3))

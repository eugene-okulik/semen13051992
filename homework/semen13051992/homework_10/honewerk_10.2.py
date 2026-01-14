def repeat_me(func):

    def wrapper(a, count):
        for i in range(count):
            func(a)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count = 5)

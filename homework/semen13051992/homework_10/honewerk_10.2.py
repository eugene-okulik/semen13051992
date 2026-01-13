def repeat_me(func):

    def wrapper(a):
        for i in range(2):
            func(a)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me')

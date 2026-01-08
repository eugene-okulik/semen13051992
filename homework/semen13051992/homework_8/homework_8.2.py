def fib(numbers):
    a, b = 0, 1
    for number in range(numbers):
        yield a
        a, b = b, a + b


print(list(fib(6))[5])
print(list(fib(201))[200])
print(list(fib(1_001))[1_000])
print(list(fib(100_001))[100_000])

def fibonacci_generator(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        a, b = b, a + b


numbers = [5, 200, 1_000, 100_000]

fib = fibonacci_generator(10000000000000000000000000000000000)
count = 1
for n in numbers:
    for num in fib:
        if count == n:
            print(num)
            break
        count += 1

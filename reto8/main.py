def obtain_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for num in range(3, int(number/2)):
        if number % num == 0:
            return False
    return True

def get_primes(number):
    while(number >=0):
        if obtain_prime(number):
            yield number
        number -= 1

def get_fibonacci(n):
    a = 0
    b = 1
    yield a
    yield b
    while n - 2 >= 0:
        a, b = (b, a + b)
        yield b
        n -= 1

def intersect():
    for i in get_primes(100):
        if i in iter(get_fibonacci(100)):
            print(i)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

intersect()

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

def get_number(num):
    prime = obtain_prime(num)
    if happy(num, 0):
        if prime:
            print("{} primo feliz".format(num))
        else:
            print("{} feliz".format(num))
    else:
        print("{} triste".format(num))


def happy(number, count):
    n = sum_squares(number)
    if n == 1:
        return True
    count += 1 if get_ones(n) else 0
    if count >= 8:
        return False
    return happy(n, count)

def sum_squares(number):
    res = 0
    for i in list(str(number)):
        res += int(i)**2
    return res

def get_ones(n):
    return "1" not in list(str(n))


for i in range(100, 0, -1):
    get_number(i)

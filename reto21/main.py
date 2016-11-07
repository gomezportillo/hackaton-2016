from functools import reduce

def split_in_lines(text):
    return text.split("\n")

def calc_degree(number):
    val, n = divisible_by_9(number)
    if val == False:
        return 0
    else:
        if  n > 17:
            return 1 + calc_degree(str(n))
        else:
            return 1

def divisible_by_9(number):
    items = [int(x) for x in list(number)]
    n = reduce(lambda x, y: x + y, items)
    return [n % 9 == 0, n]

def calc_nines(text):
    for i in text:
        val = calc_degree(i)
        if val == 0:
            print("{} -> X".format(i))
        else:
            print("{} -> {}".format(i, val))

text = open("21.in", 'r').read()

numbers = split_in_lines(text)
calc_nines(numbers)

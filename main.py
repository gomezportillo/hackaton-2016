#!/usr/bin/python
# -*- coding:utf-8 -*-

def check_sheldonness(number):
    binary = "{0:b}".format(number)

    M = 0
    N = 0

    M = len(filter(None, str(binary).split('0'))[0])

    try:
        N = len(filter(None, str(binary).split('1'))[0])
    except IndexError:
        N = 0

    lM = filter(None, str(binary).split('0'))
    for e in lM:
        if len(e) != M:
            return False

    try:
        lN = filter(None, str(binary).split('1'))
    except IndexError:
        return False

    for e in lN:
        if len(e) != N:
            return False

    return True

    print "{} {} {}".format(binary, M, N)

def main():
    lines = None
    with open('11.in') as f:
        lines = f.readlines()
        lines = lines[0].split()

    sheldon_numbers = []
    for number in range(int(lines[0]), int(lines[1])+1):
            if check_sheldonness(number):
                sheldon_numbers.append(number)

    with open('11.out', 'w') as f:
        f.write(str(sheldon_numbers))

main()

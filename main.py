#!/usr/bin/python
# -*- coding:utf-8 -*-

def generate_dictionary():
    D = {}
    D['hodoR'] = 'a'
    D['hodOr'] = 'b'
    D['hodOR'] = 'c'
    D['hoDor'] = 'd'
    D['hoDoR'] = 'e'
    D['hoDOr'] = 'f'
    D['hoDOR'] = 'g'
    D['hOdor'] = 'h'
    D['hOdoR'] = 'i'
    D['hOdOr'] = 'j'
    D['hOdOR'] = 'k'
    D['hODor'] = 'l'
    D['hODoR'] = 'm'
    D['hODOr'] = 'n'
    D['hODOR'] = 'o'
    D['Hodor'] = 'p'
    D['HodoR'] = 'q'
    D['HodOr'] = 'r'
    D['HodOR'] = 's'
    D['HoDor'] = 't'
    D['HoDoR'] = 'u'
    D['HoDOr'] = 'w'
    D['HoDOR'] = 'v'
    D['HOdor'] = 'x'
    D['HOdoR'] = 'y'
    D['HOdOr'] = 'z'
    D['HODOR'] = '!'
    D['HODOr'] = '?'
    D['HOdORhodoR'] = 'á'
    D['HOdORhoDoR'] = 'é'
    D[''] = 'í'
    D[''] = 'ó'
    D[''] = 'ú'
    D['hodor'] = ' '

    return D


def decode(D):
    msg = ""
    with open('05.in') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                msg += D[str(word)]
    return msg + "\n"

def main():
    D = generate_dictionary()
    message = decode(D)

    with open('05.out', 'w') as f:
        f.write(message)

main()

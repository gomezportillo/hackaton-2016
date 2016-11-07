#!/usr/bin/python
# -*- coding:utf-8 -*-
import itertools

def main():
    empresas = []
    alumnos = []

    with open('04.in') as f:
        lines = f.readlines()
        empresas = lines[0].split(',')
        alumnos = lines[1].split(',')

    empresas[4] = empresas[4].replace('\n', '')
    alumnos[3] = alumnos[3].replace('\n', '')
    alumnos.append('Empresa vacia')

    combinations = itertools.permutations(alumnos, len(alumnos))
    for i in combinations:
        if check_validity(i):
            print(i)

def check_validity(alumnos):
    p = alumnos.index("Alumno P")
    q = alumnos.index(" Alumno Q")
    r = alumnos.index(" Alumno R")
    t = alumnos.index(" Alumno T")
    return abs(p - q) > 1 and abs(r - t) > 2

main()

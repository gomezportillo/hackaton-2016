#!/usr/bin/python
# -*- coding:utf-8 -*-

def main():
    empresas = []
    alumnos = []

    with open('04.in') as f:
        lines = f.readlines()
        empresas = lines[0].split(',')
        alumnos = lines[1].split(',')

    empresas[4] = empresas[4].replace('\n', '')
    alumnos[3] = alumnos[3].replace('\n', '')



main()

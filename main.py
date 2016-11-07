#!/usr/bin/python
# -*- coding:utf-8 -*-

import subprocess

password = [1, 0, 0,
            0, 0, 0,
            0, 0, 0]

def execute_jar():
    cmd = ["java", "-jar", "10-CajaFuerte.jar",  "10.in", array_to_str(password)]
    last_result, err =  subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    try:
        return float(last_result[:-1])
    except ValueError:
        return last_result

def array_to_str(password):
    psw = ""
    for n in password:
        psw += str(n)
    return psw

def try_index(index, best_result):
    last_result = 0
    for number in xrange(1, 10):
        password[index] = number
        last_result = execute_jar()

        if last_result > best_result:
            return last_result

def main():
    best_result = 0

    print "Decypting... it may take a seconds, wait primo"

    for i in xrange(0, len(password)):
        best_result = try_index(i, best_result)
        print array_to_str(password)

    with open('file.out', 'w') as f:
        f.write(array_to_str(password))

main()

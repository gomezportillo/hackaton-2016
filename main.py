#!/usr/bin/python
# -*- coding:utf-8 -*-

import subprocess

def array_to_str(password):
    psw = ""
    for n in password:
        psw += str(n)
    return psw


# Redirecting stdout to var
def main():

    best_result = 0
    password = [1, 0, 0,
                0, 0, 0,
                0, 0, 0]
    cmd = ["java", "-jar", "10-CajaFuerte.jar",  "10.in", array_to_str(password)]

    last_result, err =  subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    last_result = float(last_result[:-1])
    if last_result > best_result:
        best_result = last_result
        print best_result

main()

#!/usr/bin/python
# -*- coding:utf-8 -*-

import subprocess
import string

alp_low = list(string.ascii_lowercase)
alp_upp = list(string.ascii_uppercase)
numb = range(0, 10)

all_chars = alp_low + alp_upp + numb
current_passphrase = ""

def gen_next_passphrase(n_iter, index):
    global current_passphrase

    if (n_iter > len(current_passphrase)):
        current_passphrase += all_chars[index]
    else:
        current_passphrase = current_passphrase[:-1] + str(all_chars[index])

def execute_gpg():
    cmd = ["gpg", "--passphrase", current_passphrase, "-d", "20-Cracker2.pdf.gpg"]
    out, err =  subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    if out != "":
        print "Solucionado! ", current_passphrase

def main():
    for n_iter in range(1, 11):
        for index in range(0, len(all_chars)):
            gen_next_passphrase(n_iter, index)
            print current_passphrase
            # execute_gpg()


main()

from math import gcd
from Crypto.PublicKey import RSA
import os
import itertools

name_files = []

rsa_pkeys = {}

i = 0

for file in name_files:
     i = i+1
     rsa_pub = open("./keys/"+file, "r")
     key = RSA.importKey(rsa_pub.read())

     rsa_pkeys[file] = key.n
     rsa_pub.close()

print("read keys")

for n1 in name_files:
    for n2 in name_files:
        if n1 < n2 and n1 != n2:
            cd = gcd(rsa_pkeys[n1], rsa_pkeys[n2])
            if cd != 1:
                print("n1: " + n1)
                print("n2: " + n2)
                print("cd: " + str(cd))

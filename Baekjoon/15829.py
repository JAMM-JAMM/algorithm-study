# Hashing


import string


lower_alphabet = list(string.ascii_lowercase)

integer = [i for i in range(1, 27)]

hash_table = dict(zip(lower_alphabet, integer))

r = 31

m = 1234567891

n = int(input())

s = input()

_sum =  0

for i in range(n):
    _sum += hash_table[s[i]] * (r ** i)

print(_sum % m)
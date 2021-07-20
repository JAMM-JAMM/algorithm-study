# 일곱 난쟁이
from itertools import combinations


l = []
for _ in range(9):
    l.append(int(input()))

comb_list = list(combinations(l, 7))

for i in comb_list:
    if sum(i) == 100:
        result = sorted(i)
        break

for j in result:
    print(j, end='\n')
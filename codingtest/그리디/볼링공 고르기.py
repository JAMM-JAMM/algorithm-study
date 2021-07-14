import time
from itertools import combinations

n, m = map(int, input().split())
k = list(map(int, input().split()))

start_time = time.time()

count = 0

for comb in combinations(k, 2):
    a, b = comb
    if a != b:
        count += 1

end_time = time.time()

print(count)
print(end_time - start_time)
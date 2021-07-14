import time
from itertools import permutations


n = int(input())
coins = list(map(int, input().split()))

start_time = time.time()

results = []

for i in range(1, len(coins)+1):
    temp = permutations(coins, i)
    for permu in temp:
        results.append(sum(permu))

result = set(results)

end_time = time.time()

for num in range(1, max(result)+1):
    if num not in result:
        print(num)
        break
    
print(end_time - start_time)
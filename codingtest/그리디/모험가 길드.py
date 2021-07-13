import time


n = int(input())
adv = list(map(int, input().split()))

start_time = time.time()

adv.sort()
    
result = 0
count = 0

for i in adv:
    count += 1
    if count >= i:
        result += 1
        count = 0

end_time = time.time()

print(result)
print(end_time - start_time)
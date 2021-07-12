import time

N = int(input())

start_time = time.time()

count = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

end_time = time.time()

print(count)
print(end_time - start_time)
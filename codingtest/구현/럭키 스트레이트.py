import time


n = input()

start_time = time.time()

m = int(len(n) / 2)

l, r = 0, 0

for i in range(len(n)):
    if i < m:
        l += int(n[i])
    else:
        r += int(n[i])

end_time = time.time()

print('LUCKY' if l == r else 'READY')
print(end_time - start_time)
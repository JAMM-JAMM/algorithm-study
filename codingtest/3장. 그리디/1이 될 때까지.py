import time


# 나의 풀이
n, k = map(int, input().split())

start_time = time.time()

count = 0

while n != 1:
    if n % k == 0:
        temp = int(n // k)
        n = temp
        count += 1
    else:
        n -= 1
        count += 1
    print(n)

end_time = time.time()

print(count)
print(end_time - start_time)
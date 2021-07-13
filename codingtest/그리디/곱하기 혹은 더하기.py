import time


s = str(input())

start_time = time.time()

result = 1

for i in s:
    if i == '0':
        continue
    result *= int(i)

end_time = time.time()

print(result)
print(end_time - start_time)
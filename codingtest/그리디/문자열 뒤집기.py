import time


s = input()

start_time = time.time()

count_zero = 0
count_one = 0

for i in range(len(s)):
    if i == 0:
        if s[0] == '0':
            count_one += 1
        else:
            count_zero += 1
    else:
        if s[i-1] != s[i]:
            if s[i] == '0':
                count_one += 1
            else:
                count_zero += 1

end_time = time.time()

print(end_time - start_time)
print(min(count_zero, count_one))
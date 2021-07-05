import time


# 나의 풀이
n, m = map(int, input().split())

start_time = time.time()

min_nums = []

for i in range(n):
    row = min_nums.append(min(list(map(int, input().split()))))

end_time = time.time()

print(max(min_nums))
print(end_time - start_time)

# min() 함수를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
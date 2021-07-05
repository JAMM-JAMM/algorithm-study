import time


# 나의 풀이
start_time = time.time()

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

first = numbers[0]
second = numbers[1]

result = []

for i in range(1, m+1):
    if i % 4 == 0:
        result.append(second)
    else:
        result.append(first)

end_time = time.time()

print()
print(sum(result))
print(end_time - start_time)

# 단순하게 푸는 답안 예시
start_time = time.time()

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

end_time = time.time()

print(result)
print(end_time - start_time)

# 이 문제는 M이 10,000 이하일 때, 문제를 해결할 수 있지만
# M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받게된다.

# 이 때, 해결 방법으로는 위의 답안과 아이디어는 같다.
# 가장 큰 수와 두 번째로 큰 수를 선택하면
# '6 6 6 5'라는 수열로 반복되게 된다.
# 그렇다면 m을 반복되는 수열의 길이로 나눈 몫이 반복되는 횟수는 int(m / k+1)이 되고
# 가장 큰 수가 등장하는 횟수는 int(m / k+1) * k가 된다.
# 하지만 위의 경우는 m 이 k+1로 나누어 떨어지는 경우를 나타낸 것이고,
# 만약 m이 k+1로 나누어 떨어지지 않는다면 m을 k+1로 나눈 나머지를 더해주면 된다.
# 즉, 가증 큰 수가 등장하는 횟수는 int(m / k+1) * k + m % (k + 1)이 된다.
# 그럼 두 번째로 큰 수가 등장하는 횟수도 자연스럽게 구할 수 있다. m - (int(m / k+1) * k + m % (k + 1))

# M의 크기가 커서 시간복잡도를 고려해야하는 상황에서의 코드
start_time = time.time()

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second

end_time = time.time()

print(result)
print(end_time - start_time)
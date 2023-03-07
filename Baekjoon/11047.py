# 동전 0

n, k = map(int, input().split())

result = 0

coins = list(int(input()) for _ in range(n))

coins.sort(reverse=True)

for coin in coins:
    if k == 0:
        break

    if k >= coin:
        q = (k // coin)
        k -= q * coin
        result += q

print(result)
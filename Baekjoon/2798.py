# 블랙잭

from itertools import combinations


n, m = map(int, input().split())

cards = list(map(int, input().split()))

answer = list(combinations(cards, 3))

result = sorted([sum(i) for i in answer if sum(i) <= m])

print(result[-1])



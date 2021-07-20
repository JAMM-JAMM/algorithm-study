# 날짜 계산

e, s, m = map(int, input().split())

cnt = 0
a, b, c = 0, 0, 0
while True:
    if e == a and s == b and c == m:
        break
    a += 1
    b += 1
    c += 1
    cnt += 1

    if a > 15:
        a %= 15
    if b > 28:
        b %= 28
    if c > 19:
        c %= 19

print(cnt)
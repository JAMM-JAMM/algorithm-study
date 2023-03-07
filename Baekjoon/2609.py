# 최대공약수와 최소공배수

n, m = map(int, input().split())

a, b = 0, 0

if n > m:
    a, b = m, n
else:
    a, b = n, m

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int((a * b) / gcd(a, b))

print(gcd(a, b))
print(lcm(a, b))
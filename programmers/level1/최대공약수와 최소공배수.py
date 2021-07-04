def solution(n, m):
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
        return (a * b) / gcd(a, b)
        
    return [gcd(a, b), lcm(a, b)]
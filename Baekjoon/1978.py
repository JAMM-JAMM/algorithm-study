# 소수 찾기

n = int(input())
primes = list(map(int, input().split()))

prime_nums = 0

for prime in primes:

    count = 0

    if prime == 1:
        continue
    
    for i in range(2, prime+1):
        if prime % i == 0:
            count += 1
    
    if count == 1:
        prime_nums += 1
    


print(prime_nums)

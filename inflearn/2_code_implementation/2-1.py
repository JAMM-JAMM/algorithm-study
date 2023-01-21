'''
K번째 약수
'''

# # 나의 풀이

# import sys


# sys.stdin = open("input.txt", "rt")
# n, k = map(int, input().split())

# divs = list()

# for i in range(1, n+1):
#     if n % i == 0:
#         divs.append(i)

# if len(divs) < k:
#     print(-1)
# else:
#     print(divs[k-1])

# # 다른 풀이

# import sys


# sys.stdin = open("input.txt", "rt")
# n, k = map(int, input().split())

# cnt = 0

# for i in range(1, n+1):
#     if n%i==0:
#         cnt+=1
#     if cnt==k:
#         print(i)
#         break
# else:
#     print(-1)

'''
2022-01-16 (월)
'''
import sys


sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())

cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

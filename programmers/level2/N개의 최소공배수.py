# 최대공약수를 구하는 함수 (재귀함수 + 유틀리드 호제법) 기억하기
# 최소공배수 = 두 수의 곱 /  두 수의 최대공약수

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solution(arr):
    for i in range(len(arr)-1):
        g = gcd(arr[i], arr[i+1])
        arr[i+1] = (arr[i] * arr[i+1]) / g
    answer = arr[-1]
    return answer
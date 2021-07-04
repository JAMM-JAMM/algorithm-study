# A 배열에서 작은 수 순서로 정렬
# B 배열에서 큰 수 순서로 정렬

def solution(A,B):
    answer = 0
    a = sorted(A)
    b = sorted(B, reverse=True)
    for i,j in zip(a, b):
        answer += i*j
    return answer
# 1. 테스트 코드는 통과하지만, 실행 결과 0점
# 런타임 에러가 나는 게 아님
def solution(land):
    answer = 0
    idx = 0
    for i in range(len(land)):
        if i == 0:
            idx = land[i].index(max(land[i]))
            answer += max(land[i])
            print(max(land[i]))
        else:
            del land[i][idx]
            idx = land[i].index(max(land[i]))
            answer += max(land[i])
            print(max(land[i]))
    return answer

# 2. DP 문제
def solution(land):
    
    dp = [[0 for i in range(4)] for _ in range(len(land))]
    
    for i in range(len(land)):
        if i == 0:
            for j in range(4):
                dp[i][j] = land[i][j]
        elif i > 0:
            dp[i][0] += land[i][0] + max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
            dp[i][1] += land[i][1] + max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
            dp[i][2] += land[i][2] + max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
            dp[i][3] += land[i][3] + max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
                
    return max(dp[-1])
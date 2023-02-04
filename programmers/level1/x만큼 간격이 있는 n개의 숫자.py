def solution(x, n):
    ans = []
    init_x = x
    for _ in range(n):
        ans.append(x)
        x += init_x
    return ans
def solution(n, lost, reserve):
    
    # Case 1 - 일반적인 경우, O(n)
    # lst = [1] * (n + 2)
    # for i in lost:
    #     lst[i] -= 1
    # for i in reserve:
    #     lst[i] += 1
    # for i in range(1, n+1):
    #     if lst[i-1] == 2 and lst[i] == 0:
    #         lst[i-1:i+1] = [1, 1]
    #     elif lst[i] == 0 and lst[i+1] == 2:
    #         lst[i:i+2] = [1, 1]
    # return n - lst[1:-1].count(0)
    
    # Case 2 - n의 크기가 크고, lost의 크기가 아주 작은 경우, O(nlogn)
    c = set(lost) & set(reserve)
    l = set(lost) - c
    r = set(reserve) - c
    for x in r:
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    return n - len(l)
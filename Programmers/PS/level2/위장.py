def solution(clothes):
    h_map = dict()
    
    for c in clothes:
        if c[1] not in h_map:
            h_map[c[1]] = [c[0]]
        else:
            h_map[c[1]].append(c[0])
    
    answer = 1
    
    for _, val in h_map.items():
        answer *= len(val) + 1
    
    return answer - 1
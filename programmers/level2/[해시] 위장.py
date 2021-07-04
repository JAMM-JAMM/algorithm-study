# 의상의 종류 별로 매일 다른 옷을 조합하여 나올 수 있는 경우의 수를 모두 구하면 된다.
# 경우의 수 = {(의상종류1 + 1)(의상종류2 + 1)...(의상종류N + 1)} - 1(하나도 입지 않은 경우의 수)

def solution(clothes):
    answer = 1
    categories = {}
    
    for cloth in clothes:
        if cloth[1] not in categories.keys():
            categories[cloth[1]] = 1
        else:
            categories[cloth[1]] += 1
            
    for k, v in categories.items():
        answer *= (v+1)
    
    return answer-1
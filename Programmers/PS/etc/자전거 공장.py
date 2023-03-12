def solution(cost, order):
    
    # Part 1. order 리스트의 month 값을 절대 값이 아닌 구간 값으로 변경
    order.sort()
    _order = [order[0]]
    for i, (m, n) in enumerate(order[1:]):
        _order.append([m - order[i][0], n])
        
    # Part 2. _order 리스트를 순차적으로 돌면서 뒷 쪽 구간 값의 월 별 주문량의 절대 값이 더 많은 경우
    # 앞 쪽 구간 값의 월 별 주문량에 합쳐주는 과정 반복 수행
    # 주의) 구간 값의 월이 0이 될 수 있으므로, 역수로 비교
    # _n / _m > n / m -> _m / _n < m / n
    stack = []
    for m, n in _order:
        while stack:
            _m, _n = stack[-1]
            if _m / _n < m / n:
                break
            stack.pop()
            m, n = _m + m, _n + n
        stack.append([m, n])
    
    # Part 3. cost 구간 별 가격 구하기
    answer = 0
    for m, n in stack:
        p_prev = 0
        for t, p in cost:
            if m * t >= n:
                break
            answer += (n - m * t) * (p - p_prev)
            p_prev = p
            
    return answer
        
        
        
        
        
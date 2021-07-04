def solution(answers):
    
    answer = []
    check = [0, 0, 0]
    
    def n_answer(pattern, answers):
        q, r = divmod(len(answers), len(pattern))
        return (pattern*q) + pattern[:r]
    
    a_pattern = [1,2,3,4,5]
    b_pattern = [2,1,2,3,2,4,2,5]
    c_pattern = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == n_answer(a_pattern, answers)[i]:
            check[0] += 1
    for j in range(len(answers)):
        if answers[j] == n_answer(b_pattern, answers)[j]:
            check[1] += 1
    for k in range(len(answers)):
        if answers[k] == n_answer(c_pattern, answers)[k]:
            check[2] += 1
    
    for n in range(len(check)):
        if check[n] == max(check):
            answer.append(n+1)
    
    return answer
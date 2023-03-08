from itertools import accumulate


def solution(bell):
    
    a_bell = [0]
    
    for x in bell:
        if x == 1:
            a_bell.append(-1)
        else:
            a_bell.append(1)
            
    a_bell = list(accumulate(a_bell))
    
    s_dict = dict()
    e_dict = dict()
    
    for i, x in enumerate(a_bell):
        if x not in s_dict:
            s_dict[x] = i
        e_dict[x] = i
    
    return max(e_dict[x] - s_dict[x] for x in e_dict)
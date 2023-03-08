from collections import Counter


def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    return list(dict(p_counter - c_counter).keys())[0]

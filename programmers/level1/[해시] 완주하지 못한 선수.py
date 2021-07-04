def solution(participant, completion):
    hash_participant = {}
    for p in participant:
        if p not in hash_participant:
            hash_participant[p] = 1
        else:
            hash_participant[p] += 1
    for c in completion:
        if c in hash_participant:
            hash_participant[c] -= 1
    answer = [k for k,v in hash_participant.items() if v > 0]
    return answer[0]
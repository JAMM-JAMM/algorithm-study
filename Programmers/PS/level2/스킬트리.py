def solution(skill, skill_trees):
    
    cnt = 0

    for skill_tree in skill_trees:
        tmp = ''
        for ans_skill in skill_tree:
            if ans_skill in skill:
                tmp += ans_skill
        if tmp == skill[:len(tmp)]:
            cnt += 1
    
    return cnt
def num_of_key(keymap):
    key_dict = dict()
    for m in keymap:
        for i, k in enumerate(m):
            if k not in key_dict:
                key_dict[k] = i+1
            else:
                if key_dict[k] > i+1:
                    key_dict[k] = i+1
    return key_dict

def solution(keymap, targets):
    key_dict = num_of_key(keymap)
    
    answer = []
    
    for target in targets:
        tmp = 0
        for k in target:
            if k in key_dict.keys():
                tmp += key_dict[k]
            else:
                tmp = -1
                break
        answer.append(tmp)
            
    return answer
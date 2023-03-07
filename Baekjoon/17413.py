# 단어 뒤집기 2


s = input()

result = []
tag = []
non_tag = []
tag_check = False

for i in range(len(s)):
    if s[i] == '<':
        tag.append(s[i])
        if non_tag:
            non_tag.reverse()
            result.append(non_tag)
            non_tag = []
        tag_check = True
    elif s[i] == ' ':
        if tag_check == True:
            tag.append(s[i])
        else:
            non_tag.reverse()
            non_tag.append(s[i])
            result.append(non_tag)
            non_tag = []
    elif s[i] == '>':
        tag.append(s[i])
        result.append(tag)
        tag = []
        tag_check = False
    else:
        if tag_check == True:
            tag.append(s[i])
        else:
            non_tag.append(s[i])

if non_tag:
    non_tag.reverse()
    result.append(non_tag )

for i in range(len(result)):
    print(''.join(result[i]), end='')
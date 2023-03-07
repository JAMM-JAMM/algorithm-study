# 단어 뒤집기

t = int(input())
sentences = []

for _ in range(t):
    sentences.append(input())

for sentence in sentences:
    temp = sentence.split(' ')
    result = ''
    result += temp[0][::-1]
    for i in range(1, len(temp)):
        result += ' '
        result += temp[i][::-1]
    print(result)
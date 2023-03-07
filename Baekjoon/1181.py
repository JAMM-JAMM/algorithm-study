# 단어 정렬


n = int(input())
words_list = []

for _ in range(n):
    words_list.append(input())

words_list = list(set(words_list))

answer = []

for word in words_list:
    answer.append((len(word), word))

answer.sort(key = lambda word: (word[0], word[1]))

for word in answer:
    print(word[1])
def solution(strings, n):
    temp = sorted([string[n]+string for string in strings])
    return [word[1:] for word in temp]
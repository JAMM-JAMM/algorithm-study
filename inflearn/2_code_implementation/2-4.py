'''
대표값
'''

import sys


sys.stdin = open("input.txt", "r")
n = int(input())
scores = list(map(int, input().split()))

m = round(sum(scores) / len(scores))


res_score, res_idx = -1, -1

thres = 2e9

for idx, score in enumerate(scores):
    abs_score = abs(score - m)
    if abs_score < thres:
        thres = abs_score
        res_score = score
        res_idx = idx + 1
    elif abs_score == thres:
        if res_idx > idx:
            res_idx = idx + 1
            res_score = score

print(m, res_idx)
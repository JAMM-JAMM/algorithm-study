# 회의실 배정

n = int(input())

meetings = [[0, 0] for _ in range(n)]

for meeting in meetings:
    start, end = map(int, input().split())
    meeting[0] = start
    meeting[1] = end

meetings = sorted(meetings, key=lambda x: x[0])
meetings = sorted(meetings, key=lambda x: x[1])

count = 0
end_time = 0

for meeting in meetings:
    if meeting[0] >= end_time:
        end_time = meeting[1]
        count += 1

print(count)
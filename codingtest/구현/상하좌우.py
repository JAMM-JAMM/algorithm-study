import time


# 문제 해설
# 연산 횟수는 이동 횟수에 비례하게 된다.
# 시간 복잡도: O(N)
# 시뮬레이션 유형: 일련의 명령에 따라서 개체를 차례대로 이동시킴

n = int(input()) # 정사각형 한 변의 길이
x, y = 1, 1 # 시작 좌표 초기화 (1, 1)
plans = input().split()

start_time = time.time()

move_types = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
    print(x, y)

end_time = time.time()

print(x, y)
print(end_time - start_time)


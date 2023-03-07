# 벌집

# 1: 1개의 방
# 2 ~ 7: 2개의 방 (+6)
# 8 ~ 19: 3개의 방 (+12)
# 20 ~ 37: 4개의 방 (+18)
# 38 ~ 61: 5개의 방 (+24)

n = int(input())

i = 1

room = 6
start = 0
end = 1

if n == 1:
    print(1)
else:
    while True:
        start  = end + 1
        end += i * room
        if start <= n <= end:
            print(i+1)
            break
        i += 1

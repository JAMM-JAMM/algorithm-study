# ACM 호텔

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    temp = ''
    floor = 0
    room = 1

    for _ in range(n):
        floor += 1

        if floor > h:
            floor = 1
            room += 1

    if room < 10:
        temp = str(floor) + '0' + str(room)
    else:
        temp = str(floor) + str(room)
    
    print(temp)

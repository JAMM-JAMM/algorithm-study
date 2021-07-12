from collections import deque


queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 가장 먼저 들어온 5 제거
queue.append(1)
queue.append(4)
queue.popleft() # 두 번째로 들어온 2 제거

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 순서대로 출력
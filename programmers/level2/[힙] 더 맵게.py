import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        answer += 1
        temp = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, temp)
        if scoville[0] >= K:
            return answer
    return -1
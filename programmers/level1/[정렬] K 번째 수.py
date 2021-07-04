def solution(array, commands):
    answer = []
    for comm in commands:
        start, end, order = comm
        temp_array = sorted(array[start-1:end])
        answer.append(temp_array[order-1])
    return answer
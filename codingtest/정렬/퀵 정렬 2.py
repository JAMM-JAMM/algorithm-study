array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트의 원소가 1개 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    # pivot은 첫 번째 원소로 지정
    pivot = array[0]
    # pivot을 제외한 나머지 리스트
    tail = array[1:]

    # pivot 보다 작거나 같은 수를 담는 pivot을 기준으로 분할된 왼쪽 리스트
    left_side = [x for x in tail if x <= pivot]
    # pivot 보다 큰 수를 담는 pivot을 기준으로 분할된 오른쪽 리스트
    right_side = [x for x in tail if x > pivot]

    print(left_side + [pivot] + right_side)

    # 분할된 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# [0, 3, 1, 2, 4, 5, 7, 9, 6, 8]
# [0, 3, 1, 2, 4]
# [1, 2, 3, 4]
# [1, 2]
# [6, 7, 9, 8]
# [8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
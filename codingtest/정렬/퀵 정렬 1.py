array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    
    pivot = start # pivot은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 pivot을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]
        print(array)

    # 분할 이후 왼쪽 부분에서 퀵 정렬 수행
    quick_sort(array, start, right - 1)
    # 분할 이후 오른쪽 부분에서 퀵 정렬 수행
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)

# [5, 4, 9, 0, 3, 1, 6, 2, 7, 8]
# [5, 4, 2, 0, 3, 1, 6, 9, 7, 8]
# [1, 4, 2, 0, 3, 5, 6, 9, 7, 8]
# [1, 0, 2, 4, 3, 5, 6, 9, 7, 8]
# [0, 1, 2, 4, 3, 5, 6, 9, 7, 8]
# [0, 1, 2, 4, 3, 5, 6, 9, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
# [0, 1, 2, 3, 4, 5, 6, 8, 7, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 풀이법 참고 (https://programmers.co.kr/learn/courses/30/lessons/42746)

# 원소들의 올바른 순서를 찾아서 이어붙여야하는 문제
# '이 순서를 어떻게 찾을 것인가?'를 생각
# 각 리스트에 있는 숫자들 중 가장 앞에 자릿수에 위치한 숫자가 큰 수가 앞에 위치하고
# 작은 숫자들이 뒤에 위치하도록 하자.

# 가장 간단한 방법은 string 원소 * 3을 해서 길이를 늘려주고 정렬하는 것
# 예시 [3, 30, 34, 5, 9]
# 가장 큰 수는 9-5-34-3-30이 된다.
# 이 문제에서 가장 중요한 제한 조건은 numbers의 원소는 0~999이므로,
# 하나의 숫자당 최소 3이상의 길이를 갖도록 동일하게 늘려준다는 것이다.
# 위의 원리에 따르면 9=999, 5=555, 34=343434, 3=333, 30=303030이 된다.
# 파이썬의 자체적인 정렬알고리즘을 사용하면 숫자로 이루어진 string을 비교할 때, 
# 앞의 숫자부터 차례대로 비교하면서 정렬한다.
# 따라서 정렬해보면 999, 555, 343434, 333, 303030 순서로 정렬이 된다.

def solution(numbers):
    answer = ''
    # 한 줄 반복문을 통해서 모든 원소들의 길이를 3 곱하여 새 배열을 생성해준다.
    numbers1 = [str(number)*3 for number in numbers]
    # 각 원소에 enumerate 함수로 인덱스를 붙여준다.
    numbers2 = list(enumerate(numbers1))
    # 파이썬의 자체적인 정렬알고리즘을 사용하여 정렬해준다.
    numbers2.sort(key=lambda x:x[1], reverse=True)
    # 정렬된 인덱스를 이용해서 원래의 numbers의 숫자를 통해 answer를 만들어준다.
    for idx, val in numbers2:
        answer += str(numbers[idx])
    # '0000' -> 0 같은 경우를 위해여 int로 한번 바꿔주고 다시 str로 변경
    return str(int(answer))
# 기억해둬야하는 함수
# 1. zip
# 2. startswith

# 1. 나의 풀이
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
    return answer

# 2. 다른 사람 풀이: 내장함수 zip, startswith을 이용한 풀이
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True
# 2021 카카오 채용연계형 인턴십

def solution(s):
    word = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    answer = ""
    temp = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            if temp in word.keys():
                print(temp)
                answer += str(word[temp])
                temp = ""
        
    return int(answer)
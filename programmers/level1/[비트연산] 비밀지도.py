# 2018 KAKAO BLIND RECRUITMENT

def solution(n, arr1, arr2):
    
    answer = []
    
    def conv_to_binary(array):
        result = []
        for i in range(n):
            temp = str(format(array[i], 'b'))
            temp1 = ('0' * (n - len(temp)) + temp)
            result.append(temp1)
        return result
    
    for i in range(n):
        temp_answer = ''
        for j in range(n):
            if conv_to_binary(arr1)[i][j] == '0' and conv_to_binary(arr2)[i][j] == '0':
                temp_answer += ' '
            else:
                temp_answer += '#'
        answer.append(temp_answer)
        
    return answer
from math import sqrt
from itertools import permutations


def prime_check(number):
        if number == 0 or number == 1:
            return False
        for i in range(2, int(sqrt(number))+1):
            if number % i == 0:
                return False
        return True

def solution(numbers):
    
    result = []
    
    number_list = [i for i in numbers]
    
    for i in range(1, len(numbers)+1):
        permutation_list = permutations(number_list, i)
        for permu in permutation_list:
            temp = ''
            # print(permu)
            for num in permu:
                temp += num
            # print(int(temp))
            if prime_check(int(temp)):
                result.append(int(temp))
    
    return len(set(result))
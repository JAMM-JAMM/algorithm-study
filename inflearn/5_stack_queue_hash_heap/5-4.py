'''
후위(postfix) 연산(스택)
'''

'''
풀이 날짜 : 2023-02-24
'''

import sys


sys.stdin = open("input.txt", "r")
lst = input()

stack = list()

for x in lst:
    if x.isdecimal():
        stack.append(x)
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2) + int(n1))
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2) - int(n1))
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2) * int(n1))
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2) / int(n1))

print(stack[0])
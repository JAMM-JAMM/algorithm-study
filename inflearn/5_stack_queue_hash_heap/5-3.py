'''
후위 표식 만들기 infix -> postfix (stack)
'''

'''
풀이 날짜 : 2023-02-24 (금))
'''
import sys


sys.stdin = open("input.txt", "r")
lst = input()

stack = list()
res = ''

for x in lst:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif (x == '*' or x == '/'):
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif (x == '+' or x == '-'):
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)
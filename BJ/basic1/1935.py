#1935
"""
후기표기식과 피연산자에 대응하는 값이 주어졌을 때 식을 계산
피연산자의 개수 N
두번째 줄에 후위표기식
세번째 줄부터 A부터 차례대로 해당하는 값
"""

import sys

N = int(input())
expression = input()
nums = [ int(sys.stdin.readline().strip()) for _ in range(N) ]
stack = []
# print('nums', nums)

for chr in expression:
    if "A" <= chr  <="Z":
        #스택에는 피연산자의 값을 넣는다
        stack.append(nums[ord(chr)-ord("A")])
    else:
        x = stack.pop()
        y = stack.pop()
        #연산한 값의 결과를 다시 스택에 넣는다
        if chr == "*":
            stack.append(y*x)
        elif chr == "/":
            stack.append(y/x)
        if chr == "+":
            stack.append(y+x)
        if chr == "-":
            stack.append(y-x)
  
# print(stack)
print(f"{stack[0]:.2f}")
"""
후위연산식이 주어지면 연산한 결과를 출력하시오
"""
from curses.ascii import isxdigit


nums = "352+*9-"
stack = []

for i in nums:
    # 숫자일 경우 stack에 추가
    if i.isdecimal():
        stack.append(int(i))
    else:
        two = stack.pop()
        one = stack.pop()
        if i == "+":
            res = one + two
        elif i == "-":
            res = one - two
        elif i == "*":
            res = one * two
        elif i == "/":
            res = one / two
        stack.append(res)
    
print(*stack)

"""
5-3 후위표기식
중위표기식이 입력되면 후위표기식으로 변환하시오
후위표기시근 35+ 와 같이 연산자와 피연산자 뒤에 있는 표기식이다.
중위표기식이 3+5*2이면 352*+로 표현된다
"""

a = input()
stack = []
res=""

for x in a:
    # 숫자일때
    if x.isdecimal():
        res+=x
    else:
    # 연산자일때
        if x=="(":
            stack.append(x)
        elif x=="*" or x=="/":
            while stack and (stack[-1]=="*" or stack[-1]=="/"):
                res+=stack.pop()
            stack.append(x)
        elif x=="+" or x=="-":
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.append(x)
        elif x==")":
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.pop() #여는괄호 "(" 빼내기
while stack:
    res+=stack.pop()
            

print(res)

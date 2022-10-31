#1918
"""
후위표기식
중위표기식으로 후위표기식으로 출력
"""
expression = input()
result = ""
stack = []

for c in expression:
    if c.isalpha():
      result += c
    else:
      if  c == "(":
        stack.append(c)
      elif c == "*" or c == "/":
        #스택 맨 뒤의 연산자가 * or / 일 경우 식을 나누어주어야 한다
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
          result += stack.pop()
        #스택 맨 뒤의 연산자가 + or - 일 경우 현재 연산자가 우선순위이므로 스택에 넣고 한꺼번에 빼주면 된다
        stack.append(c)
      elif c == "+" or c == "-":
        #+ or - 는 식을 나눠주는 역할(?)이니까 스택 맨 뒤의 연산자를 빼서 결과값에 넣어준다
        while stack and stack[-1] != "(":
          result += stack.pop()
        stack.append(c)
      elif c == ")":
        while stack and stack[-1] != "(":
         #괄호안의 연산이 우선이므로 닫힌 괄호 앞의 연산자(스택 맨 뒤)를 빼서 결과에 더한다
          result += stack.pop()
        #스택 맨 뒤의 값이 열린괄호면 스택에서 빼준다
        stack.pop()
while stack:
  result += stack.pop()

print(result)
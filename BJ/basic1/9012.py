#9012
"""
한 쌍의 괄호로 된 문자열을 VPS라고 한다
괄호 문자열 
"""
import sys
N = int(input())

for i in range(N):
    stack = []
    a= input()
    for j in a:
      if j == '(':
          stack.append(j)
      elif j == ')':
          if stack:
              stack.pop()
          else: 
              print("NO")
              break
    else: 
        if not stack: 
            print("YES")
        else: 
            print("NO")
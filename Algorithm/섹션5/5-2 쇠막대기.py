"""
여러개의 쇠막대기를 레이저로 절단한다
조건1 쇠막대기는 자신보다 긴 쇠막대기 위에 놓일 수 있고, 끝점은 겹치지 않는다
조건2 쇠막대기를 자르는 레이저는 적어도 하나 존재한다
조건3 레이저는 쇠막대기의 끝점에 오지 않는다 (끝점에 있으면 잘리지 않으니까..)
레이저는 여는 괄호와 닫는 괄호의 쌍 '()' 으로 표현한다
쇠막대기의 왼쪽 끝은 여는 괄호 '(' 이고, 오른쪽 끝은 닫는 괄호 ')' 이다
"""

bars = input()

# bars = "(((()(()()))(())()))(()())"

# 1 -> 시간초과
stack = []
total = 0

for i in range(len(bars)):
    # 쇠막대기가 시작되면 스택에 추가한다
    if bars[i] == "(" and bars[i+1] != ")":
        stack.append(1)
    # 레이저의 경우 스택에 있는 쇠막대기에 1씩 더한다. 스택에 쇠막대기가 없는 경우의 레이저는 무시
    elif bars[i] == "(" and bars[i+1] == ")" and stack:
        stack = [x+1 for x in stack]
    # 쇠막대기가 끝나면 스택에서 꺼내고 total 에 더한다
    elif bars[i] == ")" and bars[i-1] !="(":
        bar = stack.pop()
        total += bar

print(total)

# 1-1
for i in range(len(bars)):
    if bars[i] == "(" and bars[i+1] != ")":
        stack.append(bars[i])
    elif bars[i] == "(" and bars[i+1] == ")" and stack:
        total += len(stack)
    elif bars[i] == ")" and bars[i-1] !="(":
        bar = stack.pop()
        total += 1

print(total)

#2
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=="(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=="(":
            cnt+=len(stack)
        else:
            cnt+=1

print(cnt)

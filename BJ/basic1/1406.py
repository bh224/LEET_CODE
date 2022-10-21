# 1406
"""
L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
P $	$라는 문자를 커서 왼쪽에 추가함

첫째줄에 문자열, 그다음 명령의 개수, 명령어가 입력되고
최종 문자열을 출력

"""
import sys

st_left = list(sys.stdin.readline().strip())
st_right = []

N = int(input())

for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "L":
        if st_left:
            st_right.append(st_left.pop())
    elif order[0] == "D":
        if st_right:
            st_left.append(st_right.pop())
    elif order[0] == "B":
        if st_left:
            st_left.pop()
    elif order[0] == "P":
        st_left.append(order[1])

result = "".join(st_left + st_right[::-1])

print(result)

#17298
"""
오큰수 
크기가 N인 수열 각 원소에 대해 자신보다 큰 오른쪽 원소 중 가장 왼쪽에 있는 수
첫째 줄에 수열 A의 크기가 주어지고
둘째 줄에 수열 A의 원소가 주어지면
각 원소의 오큰수를 출력
"""
#2 스택에 인덱스
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(n)]

for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)




#1 시간초과 

# import sys
# from collections import deque

# A = int(input())
# N = list(map(int, sys.stdin.readline().split()))
# i = 0
# for n in N:
#   st = deque()
#   if i+1 <= len(N):
#     for j in N[i+1:]:
#       if n < j:
#         st.append(j)
#   if st:
#     print(st.popleft(), end=" ")
#   else: print(-1, end=" ")
#   i += 1
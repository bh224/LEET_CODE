"""
N*N개의 격자판이 있다
회전명령 정보가 2 0 3 이면
2번째 행을 왼쪽(1이면 오른쪽)으로 3만큼 회전한 뒤
모래시계모양 안 값의 합을 출력
"""

n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

s = 0
e = n-1
res = 0
for i in range(n):
    for j in range(2, e+1):
        res += a[i][j]
    if i < n//2:
        s +=1
        e-=1
    else:
        s -=1
        e+=1
print(res)


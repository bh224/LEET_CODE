"""
N*N격자판에 지역의 높이가 쓰여있다
상하좌우 숫자보다 큰 숫자는 봉우리 지역이다 병우리 지역이 몇개인지 알아내는 프로그램 작성
"""
n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
  a[x].insert(0, 0)
  a[x].append(0)

target = 0
top = 0
for i in range(n+2):
  if i == 0 or i == n-1: #a[1] ~ a[5]
    continue
  else:
    for j in range(n+2):
      if j == 0 or j == n-1:
        continue
      else:
        target = a[i][j]
        arounded = [a[i-1][j], a[i+1][j], a[i][j-1], a[i][j+1]]
        if target > max(arounded):
          top +=1

print(top)

# answer
n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
  a[x].insert(0, 0)
  a[x].append(0)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
      cnt+=1

print(cnt)

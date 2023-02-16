"""
N*N 격자판모양이고 N은 항상 홀수
격자판의 합을 출력

자연수N(홀수)가 주어지고
N줄에 걸쳐 N개의 자연수가 주어진다
격자판 안의 총 합을 출력
"""

N = int(input())
matrix=[list(map(int, input().split())) for _ in range(N)]
# a = [[1,2,3,],[4,5,6],[7,8,9]]
# 합
total = 0
# start/end 
start = end = N//2

for i in range(N):
  if i <= N//2: # 위에서부터 중간행 까지
    total += sum(matrix[i][start:end+1])
    if start == 0 and end == N-1:
      start += 1
      end -= 1
    else:
      start -= 1
      end += 1
  else:  
    total += sum(matrix[i][start:end+1])
    start += 1
    end -= 1

print(total)


# answer
n = int(input())
a=[list(map(int, input().split())) for _ in range(N)]
res = 0
s=e=n//2
for i in range(n):
  for j in range(s, e+1):
    res+=a[i][j]
  if i < n//2:
    s-=1
    e+=1
  else:
    s+=1
    e-=1
  
print(res)
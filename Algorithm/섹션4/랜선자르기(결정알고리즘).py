"""
k개의 랜선을 가지고 n개의 같은 길이의 랜선을 만들어 만들 수 있는 최대 랜선길이를 구하기
"""

a=[802, 743, 457, 539]
a.sort() # [457, 539, 743, 802]
n = 11
mx = max(a)

def count(pc):
  cnt=0
  for i in a:
    cnt += i // pc
  return cnt

pl = 1
pr = mx
result = 0

while pl<= pr:
  pc = (pl+pr) // 2 # 401
  cnt = count(pc)
  if cnt >= n:
    result = pc
    pl = pc +1
  else:
    pr = pc -1

print(result)



# answer
k, n = map(int, input().split())
line = []
res = 0
largest = 0
for i in range(k):
    tmp=int(input())
    line.append(tmp)
    largest=max(largest, tmp)
lt=1
rt=largest

def count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt
    

while lt<=rt:
    mid = (lt+rt) // 2
    if count(mid) >= n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)


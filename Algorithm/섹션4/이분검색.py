"""
N개의 수를 오름차순으로 정렬한 다음 N개의 수 중 한 개인 M이 주어지면
이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하시오

첫 줄에 N, M이 주어진다
두 번째 줄에 N개의 수가 공백을 두고 주어진다
정렬 후 M의 위치 번호를 출력
"""

n, m = map(int,input().split())
# a = int(input().split())
a = [23, 87, 65, 12, 57, 32, 99, 81]
a.sort() # [12, 23, 32, 57, 65, 81, 87, 99]
pl = 0
pr = len(a)-1

while True:
  pc = (pl+pr) // 2
  if a[pc] == m:
    print(pc+1)
    break
  elif a[pc] < m:
    pl = pc + 1
  else:
    pr = pc -1
  if pl > pr:
    break


# answer
n,m = map(int, input().split())
a=list(map(int, input().split()))
a.sort()
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt) //2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1


"""
N개의 수로 된 수열 A[1], A[2], ..., A[N]이 있다
이 수열의 1번째 수부터 j번째 수까지의 합이 M이 되는 경우의 수를 구하는 프로그램을 작성
첫째 줄에 N, M이 주어지고
다음 줄에는 수열이 공백으로 분리되어 주어진다 
"""

N, M = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
total = 0
for i in range(len(nums)):
    total += nums[i]
    if total == M:
        cnt += 1
        continue
    for j in range(1, len(nums)):
        total += nums[j]
        if total == M:
            cnt +=1
            total = 0
            break
        elif total >M:
            total = 0
            break

print(cnt)

#answer
n,m = map(int, input().split())
a = list(map(int, input().split()))
lt=0
rt=1
tot = a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+1

print(cnt)

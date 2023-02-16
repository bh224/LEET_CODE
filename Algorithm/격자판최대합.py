"""
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력
첫 줄에 자연수 N이 주어진다
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다
"""

N = int(input())
row = []
col = [0] *N
diago_1 = []
diago_2 = []

for i in range(N):
    nums = list(map(int, input().split()))
    row.append(sum(nums)) # 각 행의 합
    for j in range(N): # 각 열의 합
        col[j] += nums[j]
    #왼쪽 대각선
    diago_1.append(nums[i])
    #오른쪽 대각선
    diago_2.append(nums[-1-i])


print(row)
print(col)
print(diago_1)
print(diago_2)

res = []
res.append(max(row))
res.append(max(col))
res.append(sum(diago_1))
res.append(sum(diago_2))

print(max(res))

# answer 2차원리스트 사용
n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest = -2147000000
#행/열의 합
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
    
# 대각선의 합
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-1-i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2

print(largest)
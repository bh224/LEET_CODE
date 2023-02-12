"""
1~6까지의 주사위 3개를 던져 상금을 받는다
같은 눈 3개가 나오면 10000+나온 숫자*1000
같은 눈 2개가 나오면 1000+나온 숫자*100
모두 다른 눈이 나오면 가장 큰 숫자*100
참여하는 사람 수 N이 주어지고
던진 주사위의 결과가 각각 주어진다
가장 많은 상금을 받은 사람의 상금을 출력
"""
N = int(input())

res = []

for _ in range(N):
    nums = list(map(int, input().split()))
    cnt = 0
    num = 0
    for i in range(3):
        for j in range(i+1, 3):
            if nums[i] == nums[j]:
                num = nums[i]
                cnt += 1
    if cnt == 1:
        res.append(1000+num*100)
    elif cnt == 3:
        res.append(10000+num*1000)
    else:
        res.append(max(nums)*100)

print(max(res))

#answer
n = int(input())
res=0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a,b,c=map(int, tmp)
    if a==b and b==c:
        money=10000+a*1000
    elif a==b or a==c:
        money=1000+a*100
    elif b==c:
        money=1000+b*100
    else:
        money=c*100
    if money > res:
        res=money
print(res)


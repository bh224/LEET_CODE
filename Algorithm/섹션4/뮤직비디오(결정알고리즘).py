"""
DVD에는 N개의 곡이 들어가고 라이브에서의 순서가 그대로 유지된다

첫 째 줄에 자연수 N이 주어지고
곡의 길이가 분 단위로 주어진다
첫 번째 줄부터 DVD의 최소용량크기를 출력
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))

# a = [1,2,3,4,5,6,7,8,9]
# n = 3

def is_max(mx):
    count = 1
    total = 0
    for i in range(len(a)):
        if (total + a[i]) <= mx:
            total += a[i]
        elif (total + a[i]) > mx:
            count += 1
            total = a[i]
    return count

pl = 1
pr = sum(a)
cap = 0

while pl <= pr:
  pc = (pl+pr) // 2
  if is_max(pc) <= m:
    cap=pc
    pr = pc-1
  else:
    pl = pc+1
print(cap)

# mx = sum(a) // m

# while True:
#     result = is_max(mx)
#     if result == m:
#         print(mx)
#         break
#     elif result > m:
#         mx +=1
#     else:
#         mx -=1


# answer
n, m = map(int, input().split()))
Music=list(map(int, input().split()))

def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x > capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt


lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid) <= m:
        res=mid
        rt=mid-1
    else:
        lt = mid+1

print(res)

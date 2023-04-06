"""
4-10
1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때
1부터 n까지 각각의 수 앞에 높여있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라고 한다
예를 들어 4 8 6 2 5 1 3 7 의 역수열은 5 3 4 0 2 1 1 0 이 된다
역수열이 주어졌을 때 원래의 수열을 출력하는 프로그램을 작성
"""
n = int(input())
nums=list(map(int, input().split()))
# n=8
# nums=[5,3,4,0,2,1,1,0]

# 1

zeros=[0]*8
cnt=0

for i in range(8):
    for j in range(8):
        if nums[i] == cnt and zeros[j]==0:
            zeros[j] = i+1
            cnt=0
            break
        elif zeros[j]==0:
            cnt+=1
print(zeros)


# 2

seq=[0]*n

for i in range(n):
    for j in range(n):
        print(nums[i])  
        if nums[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            nums[i] -=1

print(seq)
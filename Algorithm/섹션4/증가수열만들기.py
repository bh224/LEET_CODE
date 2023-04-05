"""
4-9
1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어진다.
왼쪽 맨 끝 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열을 만든다.
이 때 가져온 숫자는 수열에서 제거된다

증가수열의 길이와
왼쪽에서 가져오면 L, 오른쪽이면 R 이라는 문자열을 출력
"""
n = int(input())
nums = list(map(int, input().split()))
# n=5
# nums = [2,4,5,1,3]
lt = 0
rt=n-1
last=0
result=""
temp=[]

while lt<=rt:
    if nums[lt] > last:
        temp.append((nums[lt], "L"))
    if nums[rt] > last:
        temp.append((nums[rt], "R"))
    temp.sort()
    if len(temp)==0:
        break
    else:
        result=result+temp[0][1]
        last=temp[0][0]
        if temp[0][1]=="L":
            lt +=1
        else:
            rt -=1
    temp.clear()

print(len(result))
print(result)

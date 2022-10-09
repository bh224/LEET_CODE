# 1065
"""
양의 정수 x의 각 자리수가 등차수열을 이루는 것을 한수라고한다
한 자리, 두 자리수의 경우에는 등차수열로 본다 (1~99까지는 모두 등차수열)
첫째줄에 정수 num을 입력받고 1~x까지 한수의 개수를 출력
"""

#1 
def main(x):
    count = 0
    for i in range(1, x + 1):
        if len(str(i)) <= 2:
            count += 1
        else:  # 3자리수인 경우
            nums = list(map(int, str(i)))
            if nums[1] - nums[0] == nums[2] - nums[1]:
                count += 1
    return count

num = int(input())
print(main(num))



#2
def main(x):
    count = 0
    for i in range(1, x+1): 
        if len(str(i)) <=2:
            count += 1
        else: # 3자리수 이상인 경우
            nums = list(map(int, str(i))) 
            sub = set()
            for j in range(len(str(i))-1,0, -1):
                sub.add(nums[j]-nums[j-1])
            if len(sub) == 1:
                count += 1
    return count

num = int(input())
print(main(num))

"""
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고
그 합이 최대인 자연수를 출력
함수 def digit_sum(x)를 작성

첫 줄에 자연수의 개수 N이 주어지고 다음 줄에 N개의 자연수가 주어진다
"""

def digit_sum(x):
    sum_digit = 0
    for i in x:
        sum_digit += int(i)
    return sum_digit

N = int(input())
nums = input().split()
max = 0

for i in range(N):
    res = digit_sum(nums[i])
    if res > max:
        max = res
        idx = i
        num = nums[i]

print(num)

# answer
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum=0
    while x>0:
        sum += x%10
        x = x // 10
    return sum

max = -2147000000

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)
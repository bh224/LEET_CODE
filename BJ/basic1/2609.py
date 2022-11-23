# 2609 최대공약수와 최소공배수
"""
두 자연수의 최대공약수와 최소공배수 출력
"""

A, B = list(map(int, input().split()))
# 최대공약수

def func_num(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst

#  두 수의 약수 리스트
list_a = func_num(A)
list_b = func_num(B)

# 두 리스트의 중복값 제거 후 최댓수(최소공약수)
minNum = list(set(list_a).intersection(list_b))
minNum = max(minNum)

# 최소공배수 
# A = a * 최대공약수

maxA = A // minNum
maxB = B // minNum

print(minNum, maxA * maxB * minNum)

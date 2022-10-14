# 11653
"""
정수 N이 주어졌을 때 소인수분해하여 결과를 한 줄에 하나씩 오름차순으로 출력
N이 1인 경우 암것도 출력하지 않는다

1. 소수를 하나씩 가져와서 N을 나눈다
2. 나머지가 0이 아니게 될때까지 나눈다
3. 나머지가 0이 아니면 그 다음 소수로 나눈다

"""

#1


N = int(input())
num = 2
while N !=1:
    if N % num == 0:
        N = N // num
        print(num)
    else: 
        num += 1


#2

# def PrimeNum(N):
#     if N == 1:
#         return False
#     for i in range(2, N):
#         if N % i == 0:
#             return False
#     return True

# N = int(input())
# num = 2
# while num > 0:
#     if PrimeNum(num):  # num이 소수라면
#         # print('num', num)
#         if N % num == 0 and N // num == 1:
#             print(num)
#             break
#         elif N % num == 0 and N // num != 1:
#             print(num)
#             N = N // num
#             continue
#         else:
#             num += 1
#             continue
#     else:  # num 이 소수가 아니라면...
#         num += 1
#         continue
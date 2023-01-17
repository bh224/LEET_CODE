# 6588 골든바흐의 추측
"""
4 이상의 짝수는 홀수인 소수의 합으로 나타낼 수 있다
각 테스트 케이스는 짝수 정수 n 하나로 이루어져있고 마지막 줄에는 0이 하나 주어진다
각 테스트 케이스에 대해 n = a + b 형태로 출력하고 숫자와 연산자는 공백 하나로 구분된다
만약 n을 만들 수 있는 여러 방법이 있다면 b-a가 가장 큰 것을 출력하고
두 홀 수 소수의 합으로 n을 나타낼 수 없는 경우네는 "Goldbach's conjecture is wrong."을 출력
"""
#1 -> 시간초과

import math

prime_nums = []

def PrimeNum(N):
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True


while True:
    n = int(input())
    if n == 0:
        break

    for i in range(1, n):
        if i == 1:
            continue
        if PrimeNum(i):
            if not i % 2 ==0:
                prime_nums.append(i)

    for i in prime_nums:
        a = i
        b = n - i
        if b in prime_nums:
            print(f'{n} = {a} + {b}')
            break
    else:
        print("Goldbach's conjecture is wrong.")
    

#2 에라토스테네스의 체 사용

import math

prime_nums = [True for i in range(1000001)]
prime_nums[0]=False
prime_nums[1]=False
for i in range(2, int(math.sqrt(1000000))+1): # n의 제곱근을 넘을 때까지 반복
  if prime_nums[i]:
    for k in range(i+i, 1000001, i): # 가장작은 자연수(i+i) 의 배수들을 제거
      prime_nums[k] = False


while True:
  n = int(input())
  if n == 0:
    break
  for i in range(3, len(prime_nums)): #홀수이면서 소수인 3부터 시작
    if prime_nums[i] and prime_nums[n-i]: #n = a + (n-a) 
      print(f"{n} = {i} + {n-i}") 
      break
  else:
    print("Goldbach's conjecture is wrong.")
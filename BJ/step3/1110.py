#1110
"""
0보다 크거나 같고, 99보다 작거나 같은 정수(N)가 주어질 때 다음과 같은 연산을 할 수 있다. 

먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수(a,b)로 만들고, 각 자리의 숫자를 더한다.(new_N) 그 다음, 주어진 수의 가장 오른쪽 자리 수(a)와 앞에서 구한 합의 가장 오른쪽 자리 수(b)를 이어 붙이면 새로운 수(new_N)를 만들 수 있다. 다음 예를 보자.

N이 주어졌을 때, N의 사이클의 길이 출력
"""
while True:
  N = int(input())
  if N < 0 or N > 99:  #정수가 범위를 벗어나면 다시 입력
    continue
  new_N = N  # 
  count = 0
  while True:
    a = new_N // 10
    b = new_N % 10
    sum = a + b
    new_N = b * 10 + sum %10
    count += 1
    if new_N == N:
      print(count)
      break
  break

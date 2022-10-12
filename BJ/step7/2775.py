# 2775
"""
a층의 b호에 사는 사람은 아래층(a-1)층 1호~b호까지의 사람수를 더한 값이다
0층의 b호에는 b명의 사람이 산다
0층 = [1, 2, 3, ....]

"""
T = int(input())

for _ in range(T):
  k = int(input())
  n = int(input())
  zero = [ x for x in range(1, n+1)]
  for i in range(k):
    for j in range(1,n):
      zero[j] += zero[j-1]
  print(zero[-1])
  
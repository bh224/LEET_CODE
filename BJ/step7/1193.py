#1193
"""
분수찾기
"""
N = int(input())
cycle = 1
num = N
while num > cycle:
  num -= cycle
  cycle += 1

if cycle % 2 == 0:
  list = [ i for i in range(1, cycle+1)]
  print(f"{list[num-1]}/{list[-num]}")
else:
  list = [ i for i in range(cycle, 0, -1)]
  print(f"{list[num-1]}/{list[-num]}")
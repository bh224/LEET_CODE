"""
자연수 N이 입력되면 1부터 N까지의 소수개수를 출력
"""
N = int(input())
nums = [True] * (N + 1)

def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

for i in range(N+1):
  if i == 0 or i == 1:
    nums[i] = False
  elif is_prime(i):
    for j in range(i+i, N+1, i):
      nums[j]=False

print(nums.count(True))



# answer
n = int(input())
ch = [0] * (n + 1)
cnt = 0
for i in range(2, n+1):
  if ch[i] == 0:
    cnt+=1
    for j in range(i, n+1, i):
      ch[j]=1
print(cnt)

import math

n = int(input())
nums = input().split()

def reverse(x):
  res = int(x[::-1])
  return res

def isPrime(x):
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      return False
  return True

for num in nums:
  re_num = reverse(num)
  if isPrime(re_num):
    print(re_num, end=" ")


#answer

n = int(input())
a=list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res*10+t
        x=x//10
    return  res

def isPrime(tmp):
    if tmp == 1:
        return False
    for i in range(2, x//2+1):
       if x%i==0:
          return False
    else:
       return True
    

for x in a:
  tmp = reverse(x)
  if isPrime(tmp):
     print(tmp, end=" ")

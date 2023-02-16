"""
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력
1. 첫번재 리스트의 크기 N
2. N개의 리스트 원소가 오름차순으로 주어짐
3. 두번째 리스트 크기 M
4. M개의 리스트 원소가 오름차순으로 주어짐

"""
#1
N = int(input())
num1 = list(map(int, input().split()))
M = int(input())
num2 = list(map(int, input().split()))
num1.extend(num2)
num1.sort() #sort() -> nlogn
print(num1)

#2
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = []
p1 = 0
p2 = 0
for i in range(n+m):
  if a[p1] <= b[p2]:
    c.append(a[p1])
    p1 +=1
  else:
    c.append(b[p2])
    p2 += 1
  if p1 >= n-1:
    c = c+b[p2:]
    print(*c)
    break
  elif p2 >= m-1:
    c= c+a[p1:]
    print(*c)
    break

# answer - 시간복잡도 줄이기
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = []
p1=p2 = 0

while p1 < n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
print(c)


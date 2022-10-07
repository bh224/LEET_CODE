#25304
"""
첫째 줄에 총 금액 X, 둘째 줄에 물건 종류의 수 N, 각 물건의 가격과 개수가 a,b로 주어진다
구매한 물견의 가격과 개수, 총합이 일치하면 "Yes" 아니면 "No"출력
"""
X = int(input())
N = int(input())
x = 0
n = 0
for i in range(N):
    a,b=map(int, input().split())
    n += 1
    x += a*b
if X==x and N==n:
    print("Yes")
else:
    print("No")
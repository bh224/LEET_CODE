#10950
"""
첫 째줄에 개수 T가 주어지고
두 정수 A, B를 입력받은 뒤 A+B를 출력
"""
#1
T = int(input())
total = []
for i in range(0, T):
    A, B = map(int, input().split())
    total.append(A+B)
for k in total:
    print(k)

#2
T = int(input())
for i in range(0, T):
    A, B = map(int, input().split())
    print(A+B)




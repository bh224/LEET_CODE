"""
자연수 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수다
"""
N, K = map(int, input().split())

cnt =0
for i in range(1, N+1):
    if N % i ==0:
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)

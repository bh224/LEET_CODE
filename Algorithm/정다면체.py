"""
두개의 정 N면체와 정 M면체의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력
정답이 여러개일 경우 오름차순으로 출력

자연수 N, M이 주어지고 N, M은 4, 6, 8, 12, 20 중 하나
"""
N, M = 4, 6
# N, M = map(int, input().split())

cnt = [0 for _ in range(N+M)]
max = 0

for i in range(1, N+1): 
    for j in range(1, M+1): 
        cnt[i+j-1] += 1

for i in range(N+M):
    if cnt[i] > max:
        max = cnt[i]

for i in range(N+M):
    if cnt[i] == max:
        print(i+1, end=" ")
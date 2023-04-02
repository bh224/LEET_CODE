"""
n개의 회의가 있다. 각 회의에 대해 시작시간과 종료시간이 주어지고
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대 회의 개수를 구하기

첫째 줄에 회의의 수 n이 주어지고 둘째 줄부터 각 회의의 시작시간과 종료시간이 주어진다
"""

n = int(input())
times = []
for _ in range(n):
    s, e = map(int, input().split())
    times.append((s,e))

# times = [(1,4), (2,3), (3,5), (4,6), (5,7)]

times.sort(key=lambda x:x[1])
end=0
cnt = 0

for s, e in times:
    if s >=end:
        end=e
        cnt+=1

print(cnt)
    
"""
다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나 무거운
지원자만 선발한다
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락

"""

n = int(input())
hw = []
for _ in range(n):
    h, w = map(int, input().split())
    hw.append((h,w))

# hw = [(172,67), (183,65), (180,70), (170,72), (181,60)]

hw.sort(reverse=True) # 키 순으로 정렬

max=0 # 키 순으로 정렬했으므로 몸무게만 비교하면 된다
cnt=0

for h, w in hw:
    if w > max: # 키는 나보다 크고 몸무게도 큰 사람은 탈락
        max=w
        cnt +=1

print(cnt)


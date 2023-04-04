"""
유람선에는 N명의 승객이 타고 있고 구명보트를 이용해 탈출한다.
구명보트에는 2명 이하로만 탈 수 있고 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력

N과 M이 주어지고
N개로 구성된 몸무게가 주어진다
"""
from collections import deque

n, m = 5, 150
weights = [90, 50, 70, 100, 60]

weights.sort()
weights=deque(weights)
cnt=0
while weights:
    if len(weights)==1:
        cnt+=1
        break
    if weights[0]+weights[-1]>m:
        weights.pop()
        cnt+=1
    else:
        weights.popleft()
        weights.pop()
        cnt+=1
print(cnt)

# pop은 비효율적이므로 deque 사용
# while weights:
#     if len(weights)==1:
#         cnt+=1
#         break
#     if weights[0]+weights[-1]>m:
#         weights.pop()
#         cnt+=1
#     else:
#         weights.pop(0)
#         weights.pop()
#         cnt+=1
# print(cnt)


"""
여러개의 OX문제에서 연속적으로 답을 맞히는 경우 가산점을 부여한다
앞의 문제는 틀리고 맞는 경우 1점,
연속으로 맞는 경우 첫번째는 1점, 두번째는 2점...k번째는 k점으로 계산
문제의 개수 N이 주어지고 N개 문제의 채점결과를 나타내는 0, 1이 주어진다
가산점을 고려한 총 점수를 출력
"""

from unittest import result


N = int(input(0))
scores = list(map(int, input().split()))
# scores = [1,0,1,1,1,0,0,1,1,0]
total = []
cnt = 0
total.append(scores[0])
for i in range(1, len(scores)):
    if scores[i] == 1 and scores[i-1] == 1:
        cnt += 1
        total.append(scores[i]+cnt)
    else:
        cnt = 0
        total.append(scores[i])
print(sum(total))

#answer
N = int(input(0))
a = list(map(int, input().split()))
sum=0
cnt=0
for x in a:
    if x==1:
        cnt+=1
    else:
        cnt=0
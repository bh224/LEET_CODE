"""
N명의 학생의 점수가 주어지고 학생번호는 앞에서부터 1로 시작
평균을 출력하고 평균에 가장 가까운 학생은 몇번 학생인지 출력
평균과 가장 가까운 점수가 여러개일 경우 점수가 높은 학생 > 학생번호가 빠른 학생의 번호 출력

입력
N = 10
scores = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]

출력
74 7
"""

N = int(input())
scores = list(map(int, input().split()))

avg = round(sum(scores) / N)
sub = 0
response = tuple()

for i in range(len(scores)):
    if sub == 0 or sub > abs(avg-scores[i]):
        sub = avg - scores[i]
        response = (scores[i], i)
    elif sub == abs(avg-scores[i]):
        if response[0] < scores[i]:
            response = (scores[i], i)
    else: continue

print(avg, response[1]+1)


# answer
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(scores) / n)
min = 214670000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp<min:
        min = tmp
        score=x
        res=idx+1
    elif tmp == min:
        if x > score:
            score=x
            res=idx+1

print(ave, res)
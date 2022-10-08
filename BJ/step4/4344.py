#4344.py
"""
테스트케이스의 개수 C
각 테스트마다 학생의 수 N이 첫번째 수로 주어지고 그 다음부터 N명의 점수가 주어진다
각 케이스마다 평균이 넘는 학생들의 비율 출력(소수점 셋째 자리까지)
"""
import sys

#1 
C = int(input())

for _ in range(C):
    scores = list(map(int, sys.stdin.readline().split()))
    num = scores[0]
    over_avg = [ scores[i] for i in range(1, num+1) if scores[i] >  (sum(scores)-num)/num]
    print(f"{len(over_avg)/num*100:.3f}%")


#2
C = int(input())

for _ in range(C):
    scores = list(map(int, sys.stdin.readline().split()))
    num = scores[0]
    avg = sum(scores[1:]) / num
    over_avg = 0
    for score in scores[1:]:
        if score > avg:
            over_avg += 1
    print(f"{over_avg/num*100:.3f}%")
    
#1546
"""
점수중 최대값을 M, 그러고 모든 점수를 점수/M*100으로 고친다
과목의 개수 N과 각 점수를 입력받고 새로운 평균을 출력
"""

import sys 

N = int(input())
scores = list(map(int, sys.stdin.readline().split()))
mx = max(scores)
new_scores = [ score/mx*100 for score in scores ]
print(sum(new_scores)/N)
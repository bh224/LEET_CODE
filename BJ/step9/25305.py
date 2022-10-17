#25305
"""
N명의 학생 중 가장 점수가 높은 k명 중 커트라인 점수 출력
(커트라인은 상을 받는 사람들 중 점수가 가장 낮은 사람의 점수)

응시자 수 N과 상을 받는 사람 수 k를 입력
각 학생의 점수 x가 주어진다
"""

N, k = map(int, input().split())

scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[k-1])
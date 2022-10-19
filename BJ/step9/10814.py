#10814
"""
나이와 이름이 순서대로 주어진다
나이순 -> 나이가 같으면 가입한 순서로 정렬
"""
import sys

N = int(input())

words = []
for i in range(N):
    # age, name = input().split()  #맞았는데 시간을 너무 잡아먹어서 sys 사용
    age, name = list(sys.stdin.readline().split())
    words.append((i, int(age), name))

words.sort(key=lambda x : (x[1], x[0]))

for j in words:
    print(j[1], j[2])
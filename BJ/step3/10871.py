#10871
"""
정수 N개로 이루어진 수열 A와 정수 X가 주어진다
A중 X보다 작은 수를 모두 출력
"""
#1
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i < X:
        print(i, end=" ")


#2
import sys 

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
for i in A:
    if i < X:
        print(i, end=" ")

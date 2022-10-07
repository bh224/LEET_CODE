#2438
"""
정수 N을 입력받고 첫째줄 별(*) 1개부터 N개까지 출력
"""
import sys
# N = int(input())
N = int(sys.stdin.readline())
for i in range(1, N+1):
    print("*"*i)
#15596
"""
정수n개가 주어졌을 때 n개의 합을 구하는 함수 작성
정수 n개가 저장되어있는 리스트 a
리턴값은 a에 포함되어있는 정수 n개의 합
"""

import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))



def main(list):
    result = sum(list)
    return result

main(a)
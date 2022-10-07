#10952
"""
정수 A,B를 입력받아 A+B를 출력

"""
import sys 

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A==B==0:
        break
    else: print(A+B)
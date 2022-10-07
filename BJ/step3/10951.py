#10952
"""
정수 A,B를 입력받아 A+B를 출력

"""

import sys 

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        if A or B==None:
            break
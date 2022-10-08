#3052
"""
10개의 수를 입력받은 뒤 각 수를 42로 나눈 나머지를 구하고
서로 다른 나머지가 몇 개 있는지 출력
"""

import sys

remainders = [ int(sys.stdin.readline().strip()) % 42 for _ in range(10) ]
set_remainders = set(remainders)
print(len(set_remainders))
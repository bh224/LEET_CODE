# 2739.py 
"""
정수 N을 입력받은 뒤 구구단 N단을 출력
"""

N = int(input())
for i in range(1, 10):
    print(f"{N} * {i} = {N*i} ")

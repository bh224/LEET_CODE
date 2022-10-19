#10989
"""
N개의 수가 주어졌을 때 오름차순으로
"""
import sys

N = int(input())

check_list = [0] * 10000

for i in range(N):
    input_num = int(sys.stdin.readline())
    
    check_list[input_num - 1] = check_list[input_num - 1] + 1
# print(check_list)
for i in range(10000):
    if check_list[i] != 0:
        for j in range(check_list[i]): 
            print(i+1) #인덱스를 출력
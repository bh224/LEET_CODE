#10820 문자열분석

"""
첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 
소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력
"""

import sys

while True:
    sentense = sys.stdin.readline().rstrip('\n')
    # print(">>>", sentense)
    if not sentense:
        break
    result = [0] * 4 #소문자, 대문자, 숫자, 공백
    for i in sentense:
        if i.isspace(): #공백일때
            result[3] += 1
            continue
        elif i.isdigit(): #숫자일때
            result[2] += 1
        else: #문자
            if i.islower():
                result[0] += 1
            else: result[1] += 1

    print(*result)
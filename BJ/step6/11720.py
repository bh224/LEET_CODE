#11720
"""
첫째 줄에 숫자의 개수 N
둘째 줄에 숫자 N개가 공백없이 주어진다
숫자 N개의 합을 출력
"""
#1 

def main(num, str):
    total = 0
    for i in range(num):
        total += int(str[i])
    return total

N = int(input())
n = input()
print(main(N,n))

#2

def main(str):
    result = sum(map(int, str))
    return result

N = int(input())
n = input()
print(main(n))

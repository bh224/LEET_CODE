"""
9*9 보드가 주어지고 각 행, 각 열 9개의 3*3 에 1부터 9까지 숫자가 중복되지 않는지 확인
첫 번째 줄에 완성된 9*9 스도쿠가 주어진다
YES 또는 NO 출력
"""


def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch1[a[j][i]]=1
        if sum(ch1) !=9 or sum(ch2) !=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*9
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
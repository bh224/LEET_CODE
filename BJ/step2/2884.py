# 2884
"""
45분 빠르게 알람 설정하기
두 수 시간과 분(H, M)을 입력받고 입력시간은 24시간 표기법
일어나고 싶은 시간을 입력하고, 설정해야 하는 알람을 설정
"""
#1 입출력 잘 나오는거 같은데 실패함 ㅜㅜ

H, M = map(int, input().split())

# H = 0 일때

# 2
H, M = map(int, input().split())

if M < 45:
    if H == 0:
        print(23, (M+60)-45)
    else:
        print(H-1, (M+60)-45)

else: print(H, M-45)
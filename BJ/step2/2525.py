# 2525
"""
시작하는 시간 (H, M)이 주어지고 요리에 걸리는 시간 (m)이 주어졌을 때
요리가 끝나는 시간을 출력
"""

H, M = map(int, input().split())
m = int(input())

if M+m <= 59:
    print(H, M+m)
    
else:
    H += (M+m) // 60
    M = (M+m)%60
    if H >=24:
        print(H-24, M)
    else:
        print(H, M)
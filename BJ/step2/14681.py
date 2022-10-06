# 14681
"""
주어진 점(정수x, y)이 어느 사분면에 속하는지 사분면의 번호(1,2,3,4 중 하나)를 출력
"""
while True:
        
    x = int(input())
    y = int(input())

    #x,y는 0이상
    if x == 0 or y ==0:
        continue

    #1사분면
    if x > 0 and y > 0:
        print(1)
    #4사분면
    elif x > 0 and y < 0:
        print(4)
    #2사분면
    elif x < 0 and y > 0:
        print(2)
    #3사분면
    elif x < 0 and y < 0:
        print(3)
    break




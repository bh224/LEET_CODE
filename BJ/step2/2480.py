# 2480
"""
주사위 3개를 던져서 
1. 같은 눈 세개가 나오면 10000원+(주사위숫자)*1000
2. 같은 눈 두개가 나오면 1000원 +(주사위숫자)*100
3. 모두 다른 눈이 나오면 (가장큰 주사위숫자)*100

"""
d1, d2, d3 = map(int, input().split())

if d1 == d2 == d3:
    print(10000+(d1*1000))
elif d1==d2 or d2==d3:
    print(1000+(d2*100))
elif d1==d3:
    print(1000+(d1*100))
elif d1 != d2 != d3:
    num = max(d1,d2,d3)
    print(num*100)
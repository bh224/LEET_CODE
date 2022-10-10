#5622
"""
1 다이얼 = 2초, 다음 숫자부터 1초씩 늘어난다
각 숫자마다 알파벳이 부여된다
알파벳이 주어지면 해당 숫자로 전화를 걸때 걸리는 시간을 출력
"""

dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

num = input()
time = 0

for i in num: 
    for dial in dials:
        if i in dial:
            idx = dials.index(dial)
            time += idx + 3
        else:
            continue
print(time)

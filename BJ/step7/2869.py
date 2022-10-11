#2869
"""
높이는 V
낮에 A미터 올라가고 밤에 B미터 미끄러질때
정상에 도달하는 데 필요한 일수 출력
"""
#1 -> 시간초과 반복문 x

A, B, V = map(int, input().split())
print(V, A, B)
height = 0
days = 1

while True:
    height = (A+height) - B
    print(height) #하루에 올라간 높이
    if height >= V:
        print(days)
        break
    days += 1


#2

A, B, V = map(int, input().split())
first = V -A
days = 1

tA, B, V = map(int, input().split())
first = V -A
days = 1

time = first // (A-B)
if  first % (A-B) != 0 : #하루에 올라갈 수 있는 높보다 작아도 하루 걸린 셈 친다
  print(int(time)+1+days)
else:
  print(int(time)+days)


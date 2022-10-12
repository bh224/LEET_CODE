#2839
"""
설탕 N킬로그램을 5kg, 3kg 봉지에 딱 맞게 나누어 담는데
최소 봉지개수를 출력

N이 0일 경우 (봉지를 나누어남고 남는게 없는경우) 
if문을 타고 (N이 0이니까 몫은 0이되고 bag은 변함없다) bag을 출력한 뒤 반복문은 종료된다
"""
N = int(input())
bag = 0
while N >= 0:
    if N % 5 == 0:
        bag += (N // 5)
        print(bag)
        break
    N -= 3
    bag += 1
else:
    print(-1)



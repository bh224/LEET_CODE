"""
N개의 마구간이 수직선상에 있다. 각 마구간은 x1, x2, x3...., xN의 좌표를 가지고 있고 중복은 없다.
C마리의 말이 있고 각 마구간에는 말 한마리만 넣을 수 있고 가장 가까운 두 말의 거리가 최대가 되게 배치하고 그 최댓값을 출력

첫 째줄에 N과 C가 주어지고
N개의 줄에 걸쳐 마구간의 좌표가 하나씩 주어진다다
"""
n,c = map(int, input().split())
a = []
for _ in range(n):
    num = int(input())
    a.append(num)
a.sort()

# n = 5
# c = 3
# a = [1,2,4,8,9]


def is_max(distance):
    result = 1
    pl=0
    for i in range(1, len(a)-1):
        if a[i]-a[pl] < distance:
            continue
        else:
            result +=1
            pl=i
    return result

pl=a[0]
pr=a[-1]


while pl <= pr:
    pc = (pl+pr)//2
    result = is_max(pc) 
    if result >= pc:
        max_distance = pc
        pl = pc +1
    else:
        pr = pc -1
        continue

print(max_distance)


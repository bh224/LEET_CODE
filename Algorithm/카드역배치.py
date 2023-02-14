"""
1부터 20까지의 카드가 주어지고 구간이 주어진다
해당 구간에 놓인 카드를 역순으로 배치한다
위 상태에서 다시 구간이 주어지면 해당 구간의 카드를 역순으로 재배치한다
"""

cards=[i for i in range(1, 21)]

for _ in range(10):
    start, end = map(int, input().split())
    re_range = cards[end-1:start-2:-1]
    cards[start-1:end]=[]
    cards[start-1:start-1]=re_range

print(*cards)


# answer  - 구간내 swap
a=list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i]


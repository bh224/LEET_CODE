#2292
"""
 육각형으로 이루어진 벌집이 있다. 
 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 방번호는 1씩 증가. 
 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때
 몇 개의 방을 지나가는지(시작과 끝을 포함하여) 출력

1번 방부터 출발하고 1번 방을 포함해야 하니까 room = 1

1사이클 : 1번 -> 1개
2사이클 : 2~7번 -> 6개
3사이클 : 8~19번 -> 12개
4사이클 : 20~27번 -> 18개
5사이클 : 28~61번 -> 24개
....
사이클이 한번 늘어나면 방의 개수도 6의 배수만큼 늘어난다
13번 방으로 가려면  두 사이클을 지나야하고 1번방을 포함해야 하니까 3개
58번 방으로 가려면 네 사이클을지나야하고 1번방을 포함하면 5개이다
가고싶은 방번호가 포함되어있는 사이클의 횟수만 출력하면 된다!
"""
destination = int(input())
cycle = 1 # 1번방도 포함하니까 1부터 시작
room = 1 # n번 사이클에 해당하는 방의 개수
while destination > room:
    room += 6 * cycle # 사이클이 + 1 될때마다 6의 배수로 늘어남
    cycle += 1
print(cycle)

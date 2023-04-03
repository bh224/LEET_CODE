"""
가로길이가 n인 창고가 있고 가장 높은 상자를 가장 낮은 곳으로 이동하는 높이조정을 한다
m회의 높이조정을 한 후 가장 높은 곳과 낮은 곳의 차이를 출력
"""
L = int(input())
boxs = list(map(int, input().split()))
m = int(input())
# boxs = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]

# 오름차순으로 정렬
boxs.sort()

# m회 높이조정 
for _ in range(m):
    boxs[-1] -= 1 #제일 큰 값에서 -1
    boxs[0] += 1 #제일 작은 값에서 +1
    boxs.sort() #오름차순으로 정렬

print(boxs[-1] - boxs[0])

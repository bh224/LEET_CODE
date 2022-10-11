#10250
"""
H는 층수, W는 한 층에 들어가는 방의 개수, N은 N번째 손님
초기에 호텔은 전 객실 공실상태이고
정문에서 가장 빠른 방부터 손님에게 배정하고 N번째 손님이 배정받은 객실번호 출력
"""

T = int(input())

for _ in range(T):
  H, W, N = map(int, input().split())
  floor = N % H
  num = (N // H) + 1
  if N % H == 0 :  # N번째 손님이 H의 배수인 경우 제일 끝층을 사용하게 됨
    num = N // H 
    floor = H
  print(f"{floor*100+num}")
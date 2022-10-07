#2439
"""
정수 N을 입력받고 첫째줄 별(*) 1개부터 N개까지 오른쪽 정렬로 출력
"""
N = int(input())
for i in range(1, N+1):
    print(f'{"*"*i:>{N}s}')




# num = 10
# print(f'{"*":>{num}s}')
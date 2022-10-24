#1158
"""
1번부터 N번까지 순서대로 있는 사람을 순서대로 K번째 사람을 제거
N명의 사람이 모두 제거될 때까지 반복하고 제거된 사람 순서를 구하는 프로그램
첫째줄에 N과 K가 빈 칸을 두고 주어진다

"""
N, K = map(int, input().split())
nums = [i for i in range(1, N+1)]
result = []
idx = 0
while True:
    idx += K -1
    if idx >= len(nums):
        idx %= len(nums)
    result.append(nums.pop(idx))
    if len(nums) == 0:
        break

result = list(map(str, result))
strings = ', '.join(result)
print(f'<{strings}>')
#2908
"""
입력된 숫자를 거꾸로 읽어서 큰 숫자를 출력
"""

nums = input().split()
lst = []
for i in nums:
    lst.append(int(i[::-1]))

print(max(lst))




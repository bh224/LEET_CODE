#1427
"""
정렬하려는 수 N이 주어지고 각 자리수를 내림차순으로 정렬
"""
N = input()
nums = []

for i in N:
    nums.append(int(i))

nums.sort(reverse=True)
string = ""
for i in nums:
    string += str(i)
print(string)
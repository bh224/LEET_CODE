"""
해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰수를 만든다
단, 숫자의 순서는 유지해야 한다

각 숫자들은 앞에 숫자들이 작은경우 삭제하고 앞 숫자가 된다
"""

n, m = map(int, input().split())
num = list(map(int, str(n)))

# num = [5,2,7,6,8,2,3]
# m = 3
stck=[]

for i in num:
    while stck and m>0 and stck[-1]<i:
        stck.pop()
        m -=1
    stck.append(i)

if m!=0:
    stck=stck[:-m]
result="".join(map(str, stck))
print(result)

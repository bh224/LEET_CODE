# 2588
"""
(세자리수) * (세자리수)
입력: 첫째줄에 세자리수, 둘째줄에 세자리수
출력: 각 자리수를 곱한 값과 결과값을 출력
예)
입력: 
472
385
출력:
472 * 5
472 * 8
472 * 3
472 * 385 
"""
# 1

A = int(input())
B = int(input())

b1 = B%10
b2 = (B // 10) % 10
b3 = (B // 100) % 10

print(A*b1, A*b2, A*b3, A*B, sep="\n")

# 2
A = int(input())
B = input() #문자열로 입력받음
for i in B:
    print(A*int(i))
print(A*int(B))
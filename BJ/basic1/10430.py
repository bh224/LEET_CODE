#10430 나머지
"""
(A+B)%C는 ((A%C) + (B%C))%C 와 같은지 
(A×B)%C는 ((A%C) × (B%C))%C 와 같은지
세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성
(* %는 나머지)
"""

A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
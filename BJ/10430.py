# 10430
"""
세개의 수 A,B,C를 입력받아
(A+B)%C,  ((A%C) + (B%C))%C, (A×B)%C, ((A%C) × (B%C))%C  
네 가지 값을 출력
"""
while True:
    A, B, C = map(int, input().split())
    if A < 2:
        continue
    else:
        break

print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C , sep="\n")
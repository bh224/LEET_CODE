# 10869

"""
두 자연수 A, B가 주어지고 
A+B, A-B, A*B, A/B(몫), A%B(나머지) 를 출력
"""
A, B = map(int, input().split())

print(A+B, A-B, A*B, A//B, A%B, sep="\n")
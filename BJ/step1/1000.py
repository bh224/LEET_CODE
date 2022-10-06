# 1000
"""
입력받은 두 정수 A, B의 합을 출력
런타임오류를 막으려면 A, B를 한 번에 입력 받아야 한다 (공백으로 구분)
split 함수는 리스트(iterable객체)를 반환하니까 map함수를 사용할 수 있다
"""

A, B = map(int, input().split())
print(A+B)


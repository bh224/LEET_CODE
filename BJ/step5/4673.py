#4673
"""
양의 정수 n이 주어졌을 때
n과 n의 각 자리수의 합을 구하는 것을 d(n)이라고 하면 n은 d(n)의 생성자
10000보다 작거나 같은 생성자가 없는 셀프넘버를 출력하는 함수작성

1~10000까지의 숫자를 차례대로 d(n)함수에 넣은 결과를 result 리스트에 넣는다.
i = 1 일때 d(n)은 2, 2의 생성자는 1
i = 2 일때 d(n)은 4, 4의 생성자는 2
...
즉 result 함수에 들어있지 않은 숫자는 생성자가 없는 수가 되므로
result 함수에 없는 숫자들을 출력하면 된다
"""

def d(n):
  n = n + sum(map(int, str(n)))
  return n

result = []
for i in range(1, 10):
  result.append(d(i))
print(result)

for i in range(1, 10):
  if i not in result:
    print(i)
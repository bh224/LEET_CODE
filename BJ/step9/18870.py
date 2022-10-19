#18870
"""
첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
"""
#2 

import sys

N = int(input())

words = list(map(int, sys.stdin.readline().split()))
words2 = sorted(list(set(words))) #중복제거 후 리스트로 다시 변환

print(words2)

#순서와 같이 저장
dic = {words2[i] : i  for i in range(len(words2))}

print(dic)

for j in words: #j=1000
    print(dic[j], end=" ")


#1 (시간초과)

import sys

N = int(input())

words = list(map(int, sys.stdin.readline().split()))
words2 = list(set(words))
words2.sort()

new_list = [] 
for i in range(len(words2)):
  new_list.append((i, words2[i]))

for j in words:
  for k in new_list:
    if k[1] == j:
      print(k[0], end=" ") 
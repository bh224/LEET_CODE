# 1361
"""
각문자가 연속해서 나오는 그룹단어의 개수를 출력
"""

T = int(input())
count = T
for c in range(T):
  word = input()
  for i in range(len(word)-1):  #한 글자의 경우 이 반복문은 지나지 않는다
    if word[i] == word[i+1]:
      continue
    elif word[i] != word[i+1] and word[i] in word[i+1::]:
      count -= 1
      break

print(count)

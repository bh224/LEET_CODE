#10809
"""
소문자로만 이루어진 단어 S가 주어지고
각 알파벳에 대해 단어에 포함되어 있는 경우 인덱스 위치, 포험되어 있지 않은 경우 -1을 출력
"""

word = input()
arr = [-1] *26
for i in range(len(word)):
    idx = ord(word[i])
    arr[idx-97] = word.index(word[i])

for j in arr:
    print(j, end=" ")
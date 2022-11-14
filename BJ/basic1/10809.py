#10809 알파벳 찾기

"""
알파벳 소문자로만 이루어진 단어 S가 주어지면 각 알파벳이  처음등장하는 위치를 출력
첫째줄에 단어 S가 주어지고
알파벳이 포함되어 있지 않으면 -1, 
단어에 포함되어있는 각 알파벳의 개수를 a~z 까지 공백으로 구분해서 출력
"""

alpha_nums = [-1] * 26
words = input()
for k,v  in enumerate(words):
  if alpha_nums[ord(v) - 97] == -1:
    alpha_nums[ord(v) - 97] = k
print(*alpha_nums)
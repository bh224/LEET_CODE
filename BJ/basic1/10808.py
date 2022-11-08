#10808 알파벳 개수

"""
알파벳 소문자로만 이루어진 단어 S가 주어지면 각 알파벳이 단어에 몇 개가  포함되는지 구하는 프로그램

첫째줄에 단어 S
단어에 포함되어있는 각 알파벳의 개수를 a~z 까지 공백으로 구분해서 출력
"""

alpha_nums = [0] * 26
words = input()

for i in words:
    alpha_nums[ord(i) - 97] += 1

print(*alpha_nums)
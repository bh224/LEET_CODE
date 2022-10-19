#1181
"""
알파벳 소문자로 이루어진 N개의 단어를
길이가 짧은 것 -> 길이가 같으면 사진 순 으로 정렬
"""

import sys

N = int(input())

words = set()
for _ in range(N):
    words.add(sys.stdin.readline().strip())

words_list = list(words)
words_list.sort()
words_list.sort(key=len)
# print(words_list)
for i in words_list:
    print(i)
#9093
"""
테스트개수 T
문장이 주어지면 단어를 뒤집어서 출력(단어 순서는 그대로)
"""
from operator import imod


import sys

T = int(input())
for _ in range(T):
    words = sys.stdin.readline().split()
    new_words = list(map(lambda word : word[::-1], words))
    sentence  = ' '.join(new_words)
    print(sentence)
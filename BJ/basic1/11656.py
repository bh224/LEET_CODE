#11656 접미사배열
"""
baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고, 
이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력
"""
word = input(0)
result = []
for i in range(len(word)):
    result.append(word[i::])
result.sort()

for _ in result:
    print(_)
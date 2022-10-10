#1157
"""
대소문자로 된 단어가 주어지면 이 단어에서 가장 많이 사용된 알파벳을 알아내기
가장 많이 사용된 알파벳은 대문자로 출력하고
가장 많이 사용된 알파벳이 여러 개 존재하는 경우 ?를 출력
"""
S = input().upper()
word_list = list(set(S))
count_list = []
for i in word_list:
    count = S.count(i)
    count_list.append(count)
# print(count_list)
if count_list.count(max(count_list)) >1:
    print("?")
else:
    idx = count_list.index(max(count_list))
    print(word_list[idx])
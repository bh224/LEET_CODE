# 2941
"""
입력된 문자열 중에 크로아티아 알파벳이 몇 개 포함되어 있는지 출력
"""

word = input()
c_chr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0
for i in c_chr:
    if i in word:
        count += word.count(i)
        word = word.replace(i, "*")

print(count + len(word.replace("*", "")))

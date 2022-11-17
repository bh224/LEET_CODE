#11655 ROT13
"""
영어 알파벳을 13글자씩 밀어서 만든다
ROT13 을 통하면 암호화된 내용이 원래 내용으로 돌아온다
ROT13 은 알파벳 대문자/소문자에만 적용되고 그 외의 문자는 그대로 남아있다
문자열이 주어지면 ROT13 으로 암호화하는 프로그램을 작성
"""

sentence = input()
result = ''
for i in sentence:
    if i.isupper():
        num = ord(i) + 13
        if num > 90:
            num = num - ord('Z') + ord('A') -1
            result+=chr(num)
        else:
            result+=chr(num)
    elif i.islower():
        num = ord(i) + 13
        if num > 122:
            num = num - ord('z') + ord('a') -1
            result+=chr(num)
        else:
            result+=chr(num)
    else:
        result+=i
print(result)
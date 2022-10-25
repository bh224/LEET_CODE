#17413
"""
단어뒤집기
태그는 <> 사이에 들어가 있고 태그외의 단어를 뒤집어서 춫력
"""

sentence = input()
tag = False
result = ""
stack = ""

for c in sentence:
    # 태그시작할 때(<) 태그활성화, result에 넣는다
    if c == "<":
        tag = True
        result += stack[::-1]
        stack = ""
        result += c
        continue
    # > 가 나오면 태그 종료
    elif c == ">":
        tag = False
        result += c
        continue
    # 공백이 있다는 말은 stack에 단어가 들어있다는 뜻이니까 스택에 들어있는 단어를
    # 거꾸로 꺼내서 result에 추가한뒤 스택을 비워준다
    elif c == " ":
        result += stack[::-1]+" "
        stack = ""
        continue
    
    #tag 단어일 경우 그대로 result에 넣고
    if tag:
        result += c
    #그냥 단어일 경우 스택에 넣는다
    else:
        stack += c

print(result + stack[::-1])


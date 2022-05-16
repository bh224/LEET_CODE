#125. Valid Palindrome

# Input: s = "A man, a plan, a canal: Panama"
# Output: true

#대소문자 구분x, 문자랑 숫자만 대상

# 1 리스트사용(1)

# a. 팰린드롬 -> 맨 앞 문자와 맨 뒤 문자 같음!
# b. 입력된 input값 -> 소문자로 변경 / 문자&숫자 외 제거 / 리스트 생성
# c. 문자/숫자 판별함수 isalnum() 사용 / 리스트 첫번째 뽑아내는 pop(0), 마지막 뽑아내는 pop()사용


s = "A man, a plan, a canal: Panama"

def isPalindrome(s:str):
    str = []
    for char in s:
        if char.isalnum(): #문자/숫자이면 true 
            str.append(char.lower()) #소문자로 변경후 리스트추가

    while len(str) > 1:
        if str.pop(0) != str.pop():
            return False

    return True

print(isPalindrome(s))

# 1-2 리스트사용(2)

# a. 팰린드롬을 거꾸로해도 똑같음!
# b. 1-1에서 가공한 리스트를 거꾸로 뒤집어서 두개가 일치하는지 확인!

s = "A man, a plan, a canal: Panama"

def isPalindrome(s:str):
    str = []
    for char in s:
        if char.isalnum(): #문자/숫자이면 true 
            str.append(char.lower()) #소문자로 변경후 리스트추가
    p_str = list(str)
    p_str.reverse()
    return str == p_str

print(isPalindrome(s))


# 2 정규식 & 슬라이싱 사용

# a. 처음부터 문자열을 가공 -> 소문자변환 & 정규표현식으로 문자 외 제거
# b. a로 가공된 문자열과 그걸 뒤집은 문자열이 같은지 비교! -> 슬라이싱

import re

s = "A man, a plan, a canal: Panama"

def isPalindrome(s:str):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]

print(isPalindrome(s))
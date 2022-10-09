#11654
"""
알파벳 소문자, 대문자, 숫자 0~9 중 하나가 주어졌을 때 아스키 코드값을 출력
ord() / chr() 함수 사용
"""

def main(c):
    result = ord(c)
    return result

character = input()
print(main(character))
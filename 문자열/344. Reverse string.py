# 344. 문자열 뒤집기

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# 리턴없이 리스트 내부를 조작

# 1 reverse함수 사용
# a.  입력값이 리스트니까 reverse함수를 사용


from typing import List


s = ["h","e","l","l","o"]

def reverseString(s: List[str]) -> None:
    s.reverse()
    return s

print(reverseString(s))


# 2 스왑방식
# a. 리스트내부의 가장 왼쪽-오른쪽의 요소들 자리를 바꿔주는 방식
# b. [1,2,3,4,5] 라면 1&5, 2&4 의 자리를 바꿔주면 된다

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

print(reverseString(s))
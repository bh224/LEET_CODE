# 819. 가장흔한단어

# 금지된 단어를 제외하고 가장 많이 등장하는 단어 출력(대소문자 구분x, 특수문자제외)

# a. 문자열가공 후 리스트 컴프리헨션 사용

from collections import Counter
import re
from typing import List

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    return Counter(words).most_common(1)[0][0]

print(mostCommonWord(paragraph, banned))
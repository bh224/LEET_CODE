# 49. 그룹애너그램

# 문자열 배열을 애너그램 단위로 그룹핑

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# 애너그램은 문자를 재배열한 다른 단어
# 위 예시를 예를 들자면 'eat', 'tea', 'ate' 는 'a','e','t' 를 재배열한 것으로 애너그램이다
# 애너그램은 정렬할 경우(예를 들어 오름차순으로) 'aet' 하나의 결과값만 가지게 된다
# 이를 이용해서 정렬한 결과를 key값으로 입력값(정렬전)을 value로 하면 애너그램 그룹을 만들 수 있다
# 애너그램 = {'aet':['eat','tea','ate']}

# sorted()과 sort()의 차이점 -> 둘다 리스트를 반환

# sorted()는 리스트, 문자열 둘다 사용가능, 초기값에 영향을 주지 않는다

>>> word = 'eat'
>>> sorted(word)
['a', 'e', 't']
>>> word
'eat'

# sort() 메소드는 리스트 자체를 재정렬

>>> word_list
['e', 'a', 't']
>>> word_list.sort()
>>> word_list       
['a', 'e', 't']


# ''.join()
# ''는 구분자이다 -> ''는 아무런 구분도 하지 않고 합친다는 뜻

>>> a = 'qwert'
>>> ''.join(sorted(a))
'eqrtw'
>>> '/'.join(sorted(a))  
'e/q/r/t/w'



# 1. 첫번째 방법

# 빈 딕셔너리를 만들고 정렬된 값(key)이 있는 경우, 문자열을 value로 추가하고
# 없는 경우, value값을 빈 리스트로 만든 다음 value를 추가한다

strs = ["eat","tea","tan","ate","nat","bat"]

anagram = {}

for word in strs:
    key = ''.join(sorted(word))
    if key in anagram:
        anagram[key].append(word)
    else:
        anagram[key] = []
        anagram[key].append(word)
print(list(anagram.values()))


# 2. 두번째 방법

# 첫번째 방법이 귀찮으므로.. collections.defaultdic(list)를 사용할 수 있다
# 디폴트 value값을 list로 갖는 딕셔너리를 만들어 주는데
# value값이 없어도 자동으로 빈 리스트를 갖게된다


from collections import defaultdict

anagram = defaultdict(list)

strs = ["eat","tea","tan","ate","nat","bat"]

for word in strs:
    anagram[''.join(sorted(word))].append(word)

print(list(anagram.values()))

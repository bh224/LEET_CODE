# 937. 로그파일 재정렬

# logs요소의 제일 앞자리는 식별자(dig1, let1...)
# 문자로 구성된 로그(식별자제외)가 숫자보다 먼저온다
# 문자가 동일할 경우 식별자순으로 정렬
# 숫자로그는 입력순서

# a. 문자 숫자 로그분리해서 리스트에 넣기
# b. for문 내 log는 -> dig1 8 1 5 1 
# c. b를 split() 으로 나누고 -> ['dig1', '8', '1', '5', '1'], 인덱스1의 값이 숫자인지 문자인지 판별
#     letters ['let1 art can', 'let2 own kit dig', 'let3 art zero']
#     digits ['dig1 8 1 5 1', 'dig2 3 6']
# d. lamda식을 이용해 문자리스트를 정렬 x.split()[1:](식별자제외)하고 동일한 경우 x.plit()[0](식별자순)
# e. 정렬된 letters와 digits를 더해주기



from typing import List

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:    
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

print(reorderLogFiles(logs))
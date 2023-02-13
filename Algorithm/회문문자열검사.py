"""
N개의 문자열 데이터가 앞에서 읽을 때, 뒤에서 읽을 때 같은 경우 YES, 아니면 NO출력
첫 줄에 정수 N이 주어지고 N개의 단어가 주어진다
각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다
"""

N = int(input())

for j in range(N):
    words = input().lower()
    for i in range(len(words)//2):
        if words[i] == words[-1-i]:
            continue
        else:
            print(f"#{j+1} NO")
            break
    else: print(f"#{j+1} YES")


#answer
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))


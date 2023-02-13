"""
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여
순서대로 자연수를 만들고 그 자연수의 약수 개수를 출력
문자열이 주어지면
자연수와 그 약수를 출력
"""
words = input()
num = ""
cnt = 1 #약수개수 카운트, 자기자신 포함
for i in words:
    if i.isalpha():
        continue
    else:
        num += i
num = int(num)
print(num)

for i in range(1, num//2+1):
    if num % i == 0:
        cnt += 1
print(cnt)

#answer
s=input()
res=0
for x in s:
    if x.isdecimal():
        res=res*10+int(x)
print(res)
cnt=0
for i in range(1, res=1):
    if res%i ==0:
        cnt+=1
print(cnt)

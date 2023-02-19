"""
1~9까지 자연수로 채워진 7*7 격자판이 주어지면 격자판의 가로세로방향으로
길이 5자리 회문수가 몇 개 있는지 구하시오

1~9까지 자연수로 채워진 7*7 격자판이 주어진다
5자리 회문수의 개수를 출력
"""
a = [list(map(int, input().split())) for _ in range(7)]

cnt=0

def is_anagram(data):
  l=0
  r=4
  for k in range(2):
    if data[l] != data[r]:
      return False
    else:
      l+=1
      r-=1
  print(">>",data)
  return True
  



for s in range(7):
  for i in range(3):
    c_tem = []
    r_tem = []
    for j in range(5):
      c_tem.append(a[s][i*1+j])
      r_tem.append(a[i*1+j][s])
    print(r_tem)
    if is_anagram(c_tem):
      cnt+=1
    if is_anagram(r_tem):
      cnt+=1


print(cnt)

#answer
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
  for j in range(7):
    tmp=board[j][i:i+5]
    if tmp==tmp[::-1]:
      cnt+=1
    for k in range(2):
      if board[i+k][j] != board[i+5-k-1][j]:
        break
    else:
      cnt+=1

print(cnt)
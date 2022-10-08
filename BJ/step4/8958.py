#8958
"""
퀴즈의 결과는 "OOXXOXXOOO" 와 같이 나온다
연속된 O의  개수가 1부터 연속된 점수가 된다
위의 결과의 경우 1+2+0+0+1+0+0+1+2+3 이 점수가 된다
테스트케이스 개수 N을 입력받고 각 테스트의 점수를 출력
"""

N = int(input())
for _ in range(N):
    test = input()
    total_score = []
    a = 0
    for i in test:
        if i == "O":
            a += 1
            total_score.append(a)
        elif i == "X": 
            a = 0
            total_score.append(a)
    print(sum(total_score))
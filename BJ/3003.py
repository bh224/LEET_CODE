# 3003
"""
킹, 퀸, 룩, 비숍, 나이트, 폰 = 1,1,2,2,2,8
첫째줄에 현재 가지고 있는 피스들을 입력받고
더하거나 빼야하는 개수를 출력한다
"""

K, Q, R, B, KN, P = 1,1,2,2,2,8
k,q,r,b,kn,p = map(int, input().split())
print(K-k, Q-q, R-r, B-b, KN-kn, P-p)
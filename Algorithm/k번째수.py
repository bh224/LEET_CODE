"""
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열에서 S번째부터 E번째 까지의 수를 
오름차순으로 정렬했을 때 K번째로 나타나는 숫자를 출력
T: 테스트케이스개수
N, S, E, K 가 차례대로 주어짐
N개의 숫자열
"""

T = int(input())
for i in range(1, T+1):
    N, S, E, K = map(int, input().split())
    nums = list(map(int, input().split()))
    new_nums = sorted(nums[S-1:E])

    print(f"#{i} {new_nums[K-1]}")


# anwer
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))

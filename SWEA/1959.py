'''
두 개의 숫자열
: N개의 숫자로 구성된 숫자열 Ai와 M개의 숫자로 구성된 숫자열 Bj가 있다.
Ai나 Bj를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다. 
단, 더 긴 쪽의 양끝을 벗어나서는 안된다.
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

'''


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        M, N = N, M
        A, B = B, A
    answer = -10000
    for i in range(M-N+1):
        multi_sum = 0
        for j in range(N):
            multi_sum += (B[i+j] * A[j])
        answer = max(multi_sum, answer)

    print(f'#{test_case} {answer}')

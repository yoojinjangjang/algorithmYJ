'''
숫자 배열 회전 
NXN 행렬이 주어질 때, 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라. 


'''


def get_90_rotate(N, array):
    after_rotate = []
    for i in range(N):
        after_rotate.append([array[N-x-1][i] for x in range(N)])
    return after_rotate


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    array = [input().split() for _ in range(N)]
    rotate_90_array = get_90_rotate(N, array)
    rotate_180_array = get_90_rotate(N, rotate_90_array)
    rotate_270_array = get_90_rotate(N, rotate_180_array)

    print(f'#{test_case}')
    for i in range(N):
        print("".join(rotate_90_array[i]), end=" ")
        print("".join(rotate_180_array[i]), end=" ")
        print("".join(rotate_270_array[i]), end=" ")
        print()

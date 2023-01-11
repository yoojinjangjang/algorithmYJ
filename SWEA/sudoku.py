'''
스도쿠는 숫자퍼즐로,
가로 9칸 세로 9칸으로 이루어져 있는 표에 1부터 9까지의 숫자를 채워넣는 퍼즐이다.

'''


T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    check_flag = False
    for i in range(9):
        if len(set(sudoku[i])) != 9:
            check_flag = True
            break
        if len(set([sudoku[x][i] for x in range(9)])) != 9:
            check_flag = True
            break

    if (check_flag != True):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if len(set(sum([sudoku[x][j:j+3] for x in range(i, i+3)], []))) != 9:
                    check_flag = True
                    break
            if check_flag:
                break

    if check_flag:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')

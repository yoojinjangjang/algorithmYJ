for test_case in range(1, 11):
    test_num = int(input())
    input_list = [list(map(int, input().split())) for i in range(100)]
    answer = -100000
    cross_asc = 0
    cross_desc = 0
    sum_list = []
    for i in range(100):
        cross_asc += input_list[i][i]
        cross_desc += input_list[99-i][i]
        sum_list.append(sum(input_list[i][:]))
        sum_list.append(sum(list(input_list[x][i] for x in range(100))))
    answer = max(sum_list)
    answer = max(cross_asc, cross_desc, answer)
    print(f'#{test_num} {answer}')

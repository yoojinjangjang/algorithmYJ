from collections import Counter

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_num = int(input())
    student_score = list(map(int, input().split()))
    counts = Counter(student_score)
    new_list = sorted(student_score, key=lambda x: -counts[x])
    print(f'#{test_num} {new_list[0]}')

def solution(N, M, A, B):
    result = 0

    if (N > M):
        long = A
        short = B
    else:
        long = B
        short = A

    for i in range(len(long) - len(short) + 1):
        start = i
        sum_ = 0

        for j in range(len(short)):
            sum_ += (short[j] * long[start + j])

        if (sum_ > result):
            result = sum_

    return result


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f"#{test_case} {solution(N, M, A, B)}")
## index 기준을 하나 잡고 하나씩 늘려가면서 모든 합 구하기(완전탐색)
## 시간 복잡도 (M-N+1) * N, 널널

def solution(N, M, A, B):
    max_set = set()
    if N >= M:
        for i in range(N-M+1):
            num = 0
            for j in range(M):
                num += A[i+j] * B[j]
            max_set.add(num)
    else:
        for i in range(M-N+1):
            num = 0
            for j in range(N):
                num += B[i+j] * A[j]
            max_set.add(num)

    return max(max_set)

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    answer = solution(N, M, A, B)
    print(f"#{test_case} {answer}")
## index 때문에 조금 헤맸는데 종이로 정리하고 하기

def solution(N, board):
    result = [[] for _ in range(N)]
    # print(board)
    for i in range(N):
        ans1 = []
        ans2 = []
        ans3 = []

        for fir in range(N-1, -1, -1):
            ans1.append(str(board[fir][i]))

        for sec in range(N-1, -1, -1):
            ans2.append(str(board[N-1-i][sec]))

        for thr in range(N):
            ans3.append(str(board[thr][N-1-i]))

        result[i].append("".join(ans1))
        result[i].append("".join(ans2))
        result[i].append("".join(ans3))

        # print(result)

    return result

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    answer = solution(N, board)
    print(f"#{test_case}")
    for i in range(N):
        print(*answer[i])
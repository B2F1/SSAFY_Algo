def cal_row(i, j, board, N, M): # 콕 행
    row_sum = 0
    for num in range(j-M+1, j+M):
        if 0 <= num < N:
            row_sum += board[i][num]

    return row_sum

def cal_col(i, j, board, N, M): # 콕 열
    col_sum = 0
    for num in range(i-M+1, i+M):
        if 0 <= num < N:
            col_sum += board[num][j]

    return col_sum

def cal_left(i, j, board, N, M):    # 콕 좌상 -> 우하 대각
    left_sum = 0
    for num in range(-M+1, M):
        if 0 <= i + num < N and 0 <= j + num < N:
            left_sum += board[i+num][j+num]

    return left_sum

def cal_right(i, j, board, N, M):   # 콕 좌하 -> 우상 대각
    right_sum = 0
    for num in range(-M+1, M):
        if 0 <= i - num < N and 0 <= j + num < N:
            right_sum += board[i-num][j+num]

    return right_sum

def solution(N, M, board):
    num_set = set()
    for i in range(N):
        for j in range(N):
            result_t = 0
            result_x = 0
            result_t += cal_row(i, j, board, N, M) + cal_col(i, j, board, N, M) - board[i][j]
            result_x += cal_left(i, j, board, N, M) + cal_right(i, j, board, N, M) - board[i][j]
            num_set.add(result_t)
            num_set.add(result_x)

    return max(num_set)

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    answer = solution(N, M, board)

    print(f"#{test_case} {answer}")
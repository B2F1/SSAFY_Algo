from collections import deque

def solution(N, board, A, B, C, D):
    time = 0
    queue = deque([[A, B, time]])
    directions = ([-1, 0], [1, 0], [0, -1], [0, 1])
    visited = [[False] * N for _ in range(N)]
    visited[A][B] = True

    while queue:
        x, y, t = queue.popleft()

        if x == C and y == D:
            return t

        for dx, dy in directions:
            rx, ry = x + dx, y + dy
            if 0 <= rx < N and 0 <= ry < N and not visited[rx][ry] and board[rx][ry] != 1:
                if board[rx][ry] == 2:
                    if t % 3 == 2:
                        queue.append([rx, ry, t+1])
                        visited[rx][ry] = True
                    else:
                        queue.append([x, y, t + 1])
                else:
                    queue.append([rx, ry, t + 1])
                    visited[rx][ry] = True

    return -1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    print(f"#{test_case} {solution(N, board, A, B, C, D)}")
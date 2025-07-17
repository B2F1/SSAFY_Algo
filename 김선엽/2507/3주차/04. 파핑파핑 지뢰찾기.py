## 최초 클릭을 어디로?
## 1. [0][0]
## 2. 넓게 터지는 부분 순
## 3. 연쇄 폭발 하는 곳만 선택 + 남은 "." 수 - Good!

from collections import deque

def solution(N, board, total):
    click = 0
    directions = ([-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1])
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == "*":
                continue
            elif board[i][j] == "." and not visited[i][j]:
                queue = deque([[i, j, 0]])

                while queue:
                    x, y, l = queue.popleft()

                    is_near = False
                    for dx, dy in directions:
                        rx, ry = i + dx, j + dy
                        if 0 <= rx < N and 0 <= ry < N and not visited[rx][ry]:
                            if board[rx][ry] == "*":
                                is_near = True
                                break
                    if is_near:
                        break
                    else:
                        visited[i][j] = True
                        for dx, dy in directions:
                            rx, ry = i + dx, j + dy
                            if 0 <= rx < N and 0 <= ry < N and not visited[rx][ry]:
                                queue.append([rx, ry, l+1])
                                visited[rx][ry] = True

    return total

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    total = 0
    for _ in range(N):
        row = list(input())
        total += row.count(".")
        board.append(row)

    print(f"#{test_case} {solution(N, board, total)}")
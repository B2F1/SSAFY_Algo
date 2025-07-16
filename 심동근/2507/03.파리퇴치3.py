# 하나씩 확인하는거말고 다른 방법 찾다가 결국 아래 방법 gpt

def solution(n, m, lst):
    max_flies = 0

    for y in range(n):
        for x in range(n):
            # + 모양
            plus = lst[y][x]  # 중심 칸
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                for k in range(1, m):
                    nx, ny = x + dx * k, y + dy * k
                    if 0 <= nx < n and 0 <= ny < n:
                        plus += lst[ny][nx]

            # x 모양
            cross = lst[y][x]  # 중심 칸
            for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                for k in range(1, m):
                    nx, ny = x + dx * k, y + dy * k
                    if 0 <= nx < n and 0 <= ny < n:
                        cross += lst[ny][nx]

            # 최대값 갱신
            max_flies = max(max_flies, plus, cross)

    return max_flies


## main ##
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]
    result = solution(n, m, lst)
    print(f"#{tc} {result}")

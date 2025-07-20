## By GPT

def backtrack(idx, total):
    global min_over_b

    # 가지치기: 이미 B 이상인데 더 커지면 의미 없음
    if total >= B:
        min_over_b = min(min_over_b, total)
        return

    if idx == N:
        return

    # 현재 idx 점원 선택
    backtrack(idx + 1, total + heights[idx])
    # 현재 idx 점원 선택 안 함
    backtrack(idx + 1, total)

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    min_over_b = float('inf')
    backtrack(0, 0)

    print(f"#{t} {min_over_b - B}")
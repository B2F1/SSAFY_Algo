def solution(x1, y1, r1, x2, y2, r2):
    dist = int(((x1-x2)**2 + (y1-y2)**2)**(1/2))
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1
        else:
            return 0
    elif dist == r1 + r2:
        return 1
    else:
        return 2

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(solution(x1, y1, r1, x2, y2, r2))
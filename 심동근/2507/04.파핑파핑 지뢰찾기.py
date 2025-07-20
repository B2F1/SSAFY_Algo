'''
전체 지도를 전부 탐색하며 0이 나오는 지점을 탐색
0을 발견하면 그때부터 bfs

bfs를 마친 후 .이 있는지 탐색
.이 있고 0이 남아있다면 위에 반복
        0이 없다면 남은 .의 개수 +
'''
from collections import deque

def check(lst, before_y, before_x): # 주변에 폭탄이 없는지 확인
    dx= [0, 1, 1, 1, 0, -1, -1, -1]  # 북 동 남 서
    dy= [-1, -1, 0, 1, 1, 1, 0, -1]
    cnt= 0

    for i in range(8):
        y= dy[i] + before_y
        x= dx[i] + before_x
        if (0<=y and y<N and 0<=x and x<N):
            if (lst[y][x]=="*"):
                cnt+=1
    return cnt

def bfs(N, lst, y, x):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]  # 북 동 남 서
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    lst[y][x]= "0"
    queue= deque()
    queue.append((y,x))

    while(queue):
        current_y, current_x = queue.popleft()
        for i in range(8):
            new_y= dy[i]+current_y
            new_x= dx[i]+current_x
            if (0 <= new_y and new_y < N and 0 <= new_x and new_x < N and lst[new_y][new_x] == "."):
                bomb_cnt= check(lst, new_y, new_x)
                lst[new_y][new_x]= str(bomb_cnt)
                if(bomb_cnt==0):
                    queue.append((new_y, new_x))

def solution(N, lst):
    cnt= 0

    for y in range(N):
        for x in range(N):
            if(lst[y][x]=="." and check(lst, y, x)==0):
                bfs(N, lst, y, x)
                cnt+=1

    for y in range(N):
        for x in range(N):
            if(lst[y][x]=="."):
                cnt+=1

    return cnt
## main ##
T = int(input())
for test_case in range(1, T + 1):
    N= int(input())
    board= []
    for i in range(N):
        temp= list(input().strip())
        board.append(temp)
    print(f"#{test_case} {solution(N, board)}")

# N= 3
# lst=[[".",".","*"],
# [".",".","*"],
# ["*","*","."]]
# print(solution(N, lst))
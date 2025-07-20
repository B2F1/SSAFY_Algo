'''
장애물 == 1
소용돌이 == 2(0초에 생성된 소용돌이는 0, 1초 유지되고 2초에 사라진다 그리고 다시 3, 4초)

기존 bfs와 다르게 고려해야 할 부분은 소용돌이
그 말은 4방향으로 움직이는 것 외에 현 자리에 가만히 존재하는 하나의 선택지가 더 있다는 말
소용돌이는 현재 초가 2, 5, 8... 으로 커지는 순간에는 없다. 즉 current_time이 해당값에 속한 경우에는 멈추는 경우 고려 x

이 방식이 아니라 bfs 매개변수로 현재 초를 넣으면 더 좋을 듯
만약 앞선 방식으로 진행하면 방문처리가 상당히 까다로워지기에 bfs에 현재 초를 둬서 시간을 각자 다르게 설정하여 문제풀 것

==> 문제 발견! 이런 경우 소용돌이를 계속 마주쳐서 시간이 오래 걸리는 녀셕이 가장 먼저 도달했다고 결정이 날 수 있음

'''
import copy
from collections import deque
import heapq


def solution(N, board, start_y, start_x, end_y, end_x):

    # queue= deque()
    # queue.append((start_y, start_x, 0))

    queue= []
    heapq.heappush(queue, (0, start_y, start_x))

    dy= [-1, 0, 1, 0] # 북 동 남 서
    dx= [0, 1, 0, -1]
    is_visited = [[0]*N for _ in range(N)]

    while(queue):
        time, y, x= heapq.heappop(queue)

        if(is_visited[y][x]!=0): # 이미 방문한 곳인지 확인
            continue

        if(y==end_y and x==end_x):
            return time

        time+=1
        is_visited[y][x]= 1

        for i in range(4):
            new_y= dy[i]+y
            new_x= dx[i]+x
            if(0<= new_y < N and 0<= new_x < N):

                if(board[new_y][new_x]==2): # 소용돌이인 경우
                    if((time+1)%3==0):
                        heapq.heappush(queue, (time, new_y, new_x))
                        # queue.append((new_y, new_x, time))
                    elif((time+1)%3==1):
                        heapq.heappush(queue, (time+1, new_y, new_x))
                        # queue.append((new_y, new_x, time+1))
                    elif((time+1)%3==2):
                        heapq.heappush(queue, (time+2, new_y, new_x))
                        # queue.append((new_y, new_x, time+2))

                else: # 소용돌이가 아닌 경우
                    heapq.heappush(queue, (time, new_y, new_x))
                    # queue.append((new_y, new_x, time))

## main ##
T = int(input())
for test_case in range(1, T + 1):
    N= int(input())
    board= []
    for i in range(N):
        board.append(list(map(int, input().split())))
    start_y, start_x= map(int, input().split())
    end_y, end_x= map(int, input().split())
    print(f"#{test_case} {solution(N, board, start_y, start_x, end_y, end_x)}")

# N= 5
# board= [[0,0,0,0,0],
#         [0,0,0,1,0],
#         [0,0,0,1,0],
#         [2,2,1,1,0],
#         [0,0,0,0,0]]
# start_y= 4
# start_x= 0
# end_y= 2
# end_x= 0
# print(solution(N, board, start_y, start_x, end_y, end_x))
'''
각각의 겉테두리부터 꺼내서 배열에 넣기
len()구하고 각 리스트 회전
결합
'''
from collections import deque


def getSkin(N, M, start, lst): # 세로(y), 가로(x) == (5, 4)
    result= []

    # 상
    for i in range(start, M-start-1):
        result.append(lst[start][i])

    # 오른쪽
    for i in range(start, N-start-1):
        result.append(lst[i][M-start-1])

    # 하
    for i in range(M-1-start, start, -1):
        result.append(lst[N-1-start][i])

    # 왼쪽
    for i in range(N-1-start, start, -1):
        result.append(lst[i][start])

    return result

def setSkin(N, M, start, lst, result):
    # 상
    for i in range(start, M-start - 1):
        result[start][i]= lst.popleft()

    # 오른쪽
    for i in range(start, N-start - 1):
        result[i][M-start-1]= lst.popleft()

    # 하
    for i in range(M-1-start, start, -1):
        result[N-1-start][i]= lst.popleft()

    # 왼쪽
    for i in range(N-1-start, start, -1):
        result[i][start]= lst.popleft()

    return result

def cycle(lst, len_, move):
    turns= 0

    if(len_>move):
        turns= move
    else:
        turns= (move%len_)

    lst= deque(lst)
    for i in range(turns):
        lst.append(lst.popleft())
    return lst

def solution(N, M, move, lst):

    # 1. 껍데기가 몇 개인지 구하기(min_ == 껍데기 개수)
    temp= min(N, M)
    min_= temp//2

    # 2. 껍데기 구하기
    cube= []
    for i in range(0, min_):
        cube.append(getSkin(N, M, i, lst))

    # 3. 각 껍데기 회전
    for i in range(len(cube)):
        cube[i]= cycle(cube[i], len(cube[i]), move)

    # 3. 다시 끼워넣기
    result= lst

    for i in range(0, min_):
        result= setSkin(N, M, i, cube[i], result)

    return result


## main ##
N, M, move= map(int, input().split())
lst= []
for i in range(N):
    temp= list(map(int, input().split()))
    lst.append(temp)
result= solution(N, M, move, lst)

for i in result:
    print(*i)

# N, M= 5, 4
# move= 7
# lst=[[1,2,3,4],
#      [7,8,9,10],
#      [13,14,15,16],
#      [19,20,21,22],
#      [25,26,27,28]]
# print(solution(N, M, move, lst))


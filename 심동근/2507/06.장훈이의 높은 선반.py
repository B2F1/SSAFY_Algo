from itertools import combinations


def solution(N, B, height):
    result= []

    for i in range(1, N+1):
        for comb in combinations(height, i):
            sum_= sum(comb)
            if(sum_>=B):
                result.append(sum_)

    # print(result)
    return min(result)-B

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, B= map(int, input().split())
    height= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, B, height)}")
# N, B= 5, 16
# height= [1,3,3,5,6]
# print(solution(N, B, height))





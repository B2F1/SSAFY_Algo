

def solution(n, lst):
    result= [[] for i in range(n)]

    result_1= []
    for i in range(n):
        temp= ""
        for j in range(n-1, -1, -1):
            temp+=str(lst[j][i])
        result_1.append(temp)

    # print(result_1)

    result_2= []
    for i in range(n-1, -1, -1):
        temp= ""
        for j in range(n-1, -1, -1):
            temp+= str(lst[i][j])
        result_2.append(temp)
    # print(result_2)

    result_3= []
    for i in range(n-1, -1, -1):
        temp = ""
        for j in range(n):
            temp += str(lst[j][i])
        result_3.append(temp)
    # print(result_3)

    for i in range(len(lst)):
        result[i].append(result_1[i])
        result[i].append(result_2[i])
        result[i].append(result_3[i])

    # print(result)

    for row in result: # gpt's help
        print(" ".join(row))  # 리스트를 공백으로 합쳐서 출력

## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n= int(input())
    lst= []
    for i in range(n):
        temp= list(map(int, input().split()))
        lst.append(temp)
    print(f"#{test_case}")
    solution(n, lst)

# lst = [
#     [6, 9, 4, 7, 0, 5],
#     [8, 9, 9, 2, 6, 5],
#     [6, 8, 5, 4, 9, 8],
#     [2, 2, 7, 7, 8, 4],
#     [7, 5, 1, 9, 7, 9],
#     [8, 9, 3, 9, 7, 6]
# ]
#
# print(solution(6, lst))
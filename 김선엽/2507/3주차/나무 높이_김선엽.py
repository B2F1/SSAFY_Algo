# import sys
# sys.stdin = open("data/Sample_input.txt", "r")

### 올려야 하는 나무의 높이를 2로 나눈 몫과 나머지로 나누어 표현했습니다.
### 즉, 2 3 10 5라는 나무들이 있을 때, 올려야 하는 높이는 각 8 7 0 5 입니다.
### 여기서, 8은 몫 4 나머지 0, 7은 몫 3 홀수 나머지 1 ... 모두 구하면 몫 9, 나머지 2가 됩니다.
### 이 두 수를 가지고 해결했습니다.

def solution(N, trees):
    tallest = max(trees)
    even = 0
    odd = 0
    ok = False # 모든 나무의 키가 같지 않음을 확인 하기 위한 변수 입니다.
    total = 0
    for tree in trees:
        if tree < tallest:
            ok = True
            minus = tallest - tree
            total += minus
            even += minus // 2
            odd += minus % 2
    if not ok:  # 모든 나무의 키가 같으므로 0을 return 합니다.
        return 0
    else:
        if even > odd:  ## 처리해야 하는 짝수가 더 많을 경우입니다.
            result = 2 * odd    ## 우선 홀수의 2배를 더합니다(1,2,1,2)
            even -= odd ## 1,2,1,2로 처리했기 때문에 2로 처리한 횟수, 즉, odd를 빼줬습니다.
            even = even * 2 ## 이제 짝수를 총 자라야 하는 길이로 처리하기 위해 2를 곱합니다.
            result += (even // 3) * 2   ## 여기서 1과 2가 남았을 때는 날짜를 조절 가능하기 때문에, 3으로 나눕니다.
            even %= 3 ## 남은 날짜를 1 혹은 2가 남도록 수정합니다.
            if even == 1: ## 1이 남았을 경우 하루 뒤에 물을 주고 return
                result += 1
            elif even == 2: ## 2가 남았을 경우 하루를 쉬고 다음날 물을 주고 return
                result += 2
            return result
        elif even < odd: # 짝수가 더 많을 경우입니다.
            result = 2 * even # 동일하게 짝수 일만큼 더합니다.
            odd -= even # 홀수를 짝수만큼 빼줍니다(1 2 1 2)
            if odd > 1: # 1보다 크다면
                result += 2 * (odd - 1) + 1 ## 1 0 1 0 1 식으로 주고 안주고를 반복합니다,.
            else: # 홀수가 1이면 하루 더 주고 return 합니다.
                result += 1

            return result
        else:
            return 2 * even

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    print(f"#{test_case} {solution(N, trees)}")
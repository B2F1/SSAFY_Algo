## combinations(순열)로 선거구를 둘로 나눠 연결 가능 검증 후 인구 수 저장

from itertools import combinations
from collections import deque

def solution(N, population, bridge, total):
    result = set()
    cities = [i+1 for i in range(N)]

    if N % 2 == 1:
        a = N // 2 + 1
    else:
        a = N // 2

    gap = -1
    for i in range(a, N):
        for comb in combinations(cities, i):
            city_a = set(comb)
            a = sum(city_a)
            city_b = []
            for k in range(N):
                if k + 1 not in city_a:
                    city_b.append(k+1)
            b = sum(city_b)

            queue = deque([comb[0]])

            while queue and city_a:
                cur= queue.popleft()
                city_a.remove(cur)

                for next_ in bridge[cur-1]:
                    if next_ in comb and next_ in city_a:
                        queue.append(next_)
                        city_a.remove(cur)

            if not city_a:
                queue = deque([city_b[0]])
                city_b = set(city_b)

                while queue and city_b:
                    cur= queue.popleft()
                    city_b.remove(cur)

                    for next_ in bridge[cur - 1]:
                        if next_ in comb and next_ in city_a:
                            queue.append(next_)
                            city_b.remove(cur)

            if not (city_a and city_b):
                result.add(abs(a-b))

    if result:
        return min(result)
    else:
        return -1

N = int(input())
population = list(map(int, input().split()))
total = sum(population)
bridge = []
for _ in range(N):
    bridge.append(list(map(int, input().split())))
print(solution(N, population, bridge, total))
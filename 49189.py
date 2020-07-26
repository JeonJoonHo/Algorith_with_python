# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

import heapq

def solution(n, edge):
    answer = 0

    graph = {(i + 1): set() for i in range(n)}

    for value in edge:
        graph[value[0]].add(value[1])
        graph[value[1]].add(value[0])

    queue = []
    distances = [9999] * (n + 1)
    distances[1] = 0
    heapq.heappush(queue, [0, 1])

    max_distance = 0
    while queue:
        mid = heapq.heappop(queue)
        for end in graph[mid[1]]:
            if distances[end] > mid[0] + 1:
                distances[end] = mid[0] + 1
                heapq.heappush(queue, [distances[end], end])
                if max_distance < distances[end]:
                    max_distance = distances[end]

    return distances.count(max_distance)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

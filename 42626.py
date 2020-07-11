# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while True:
        current = heapq.heappop(scoville)
        if K <= current:
            break

        if len(scoville) <= 0:
            answer = -1
            break

        mix = current + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        answer += 1

    return answer

print(solution([1, 0, 3, 9, 2, 12]	, 10))


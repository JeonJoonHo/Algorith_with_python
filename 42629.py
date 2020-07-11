# https://programmers.co.kr/learn/courses/30/lessons/42629?language=python3

import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    current_index = 0

    priority_queue = []
    while stock < k:
        for i in range(current_index, len(dates)):
            if stock < dates[i]:
                break

            heapq.heappush(priority_queue, (-supplies[i], supplies[i]))
            current_index += 1

        stock += heapq.heappop(priority_queue)[1]
        answer += 1

    return answer

print(solution(4, [4, 10, 15], [20, 5, 10], 30))

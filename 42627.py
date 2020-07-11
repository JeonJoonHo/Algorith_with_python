# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

import heapq

def solution(jobs):
    answer = 0
    complete_job_count = 0

    priority_queue = []
    time = 0
    accumulate_works = -1

    while complete_job_count < len(jobs):
        for job in jobs:
            if accumulate_works < job[0] <= time:
                answer += time - job[0]
                heapq.heappush(priority_queue, job[1])

        if len(priority_queue) > 0:
            answer += len(priority_queue) * priority_queue[0]
            accumulate_works = time
            time += heapq.heappop(priority_queue)
            complete_job_count += 1
        else:
            time += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
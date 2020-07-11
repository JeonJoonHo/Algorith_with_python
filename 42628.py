# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

import heapq


def solution(operations):
    max_priority_queue = []
    min_priority_queue = []

    remove_value_counts = 0
    insert_value_counts = 0

    for operation in operations:
        if remove_value_counts >= insert_value_counts:
            min_priority_queue = []
            max_priority_queue = []

        if operation.find('I') >= 0:
            number = operation.split(' ')[-1]
            heapq.heappush(max_priority_queue, -(int(number)))
            heapq.heappush(min_priority_queue, int(number))

            insert_value_counts += 1
        elif operation.find('-1') >= 0 and len(min_priority_queue) > 0 and remove_value_counts < insert_value_counts:
            heapq.heappop(min_priority_queue)
            remove_value_counts += 1
        elif operation.find('1') >= 0 and len(max_priority_queue) > 0 and remove_value_counts < insert_value_counts:
            heapq.heappop(max_priority_queue)
            remove_value_counts += 1

    if remove_value_counts >= insert_value_counts:
        answer = [0, 0]
    else:
        answer = [-heapq.heappop(max_priority_queue), heapq.heappop(min_priority_queue)]

    return answer

print(solution(["I 1","I 1","I 1","I 1", "D 1","D 1","D 1","D 1","D 1","I 1","I 1","D -1","D 1","I 3"]))

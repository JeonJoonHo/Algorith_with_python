# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

from queue import Queue

def solution(priorities, location):
    answer = 0

    complete_task = 0

    papers = Queue()
    for index, priority in enumerate(priorities):
        papers.put({'priority': priority, 'order': index})

    while answer == 0:
        is_bigger_priority = False

        current_paper = papers.get()
        for paper in list(papers.queue):
            if paper['priority'] > current_paper['priority']:
                is_bigger_priority = True
                break

        if is_bigger_priority:
            papers.put(current_paper)
        else:
            complete_task += 1
            if location == current_paper['order']:
                answer = complete_task

    return answer

print(solution([2, 1, 3, 2], 2))
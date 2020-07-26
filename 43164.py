# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        current = stack[-1]
        if current not in graph or len(graph[current]) == 0:
            visited.append(stack.pop())
        else:
            stack.append(graph[current].pop())

    return visited

def solution(tickets):
    cities = set()
    for ticket in tickets:
        cities |= set(ticket)

    graph = {city: [] for city in cities}

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for key, value in graph.items():
        value.sort(reverse=True)

    answer = DFS(graph, 'ICN')
    answer.reverse()
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

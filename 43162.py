# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

def DFS(graph, root, connect, current_network):
    visited = []
    stack = [root]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            connect[current] = current_network
            stack += graph[current] - set(visited)
    return visited


def solution(n, computers):
    connect = [0] * (n + 1)

    graph_list = {}
    for i in range(n):
        connection_list = set()
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                connection_list.add(j + 1)

        graph_list[i + 1] = connection_list

    network_number = 0
    for key, value in graph_list.items():
        if connect[key] > 0:
            continue
        network_number += 1
        DFS(graph_list, key, connect, network_number)

    return network_number

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

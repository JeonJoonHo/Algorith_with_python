# https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3

def solution(n, costs):
    answer = 0

    connected = [0] * n

    costs.sort(key=lambda x: x[2])

    connected[0] = 1
    while sum(connected) != n:
        for cost in costs:
            if connected[cost[0]] == 1 or connected[cost[1]] == 1:
                if connected[cost[0]] == 1 and connected[cost[1]] == 1:
                    continue
                else:
                    connected[cost[0]] = 1
                    connected[cost[1]] = 1
                    answer += cost[2]
                    break

    return answer

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

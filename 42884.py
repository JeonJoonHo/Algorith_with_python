# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3#

def solution(routes):
    answer = 1

    route_lenght = len(routes)
    routes.sort(key=lambda route: int(route[0]))

    end = routes[0][1]
    for i in range(1, route_lenght):
        current = routes[i]

        if current[0] <= end:
            end = min(current[1], end)
        else:
            answer += 1
            end = current[1]

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))

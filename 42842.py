# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

def solution(brown, yellow):
    for v_y in range(1, int(yellow ** 0.5) + 1):
        if yellow % v_y == 0:
            h_y = yellow // v_y
            if ((h_y + 2) * 2) + (v_y * 2) == brown:
                return [h_y + 2, v_y + 2]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

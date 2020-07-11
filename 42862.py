# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):

    temp_lost = []
    for i in lost:
        try:
            if reserve.index(i) >= 0:
                reserve.remove(i)
                continue
        except:
            ''

        temp_lost.append(i)

    lost = temp_lost
    answer = n - len(lost)

    for i in lost:

        try:
            if reserve.index(i - 1) >= 0:
                answer += 1
                reserve.remove(i - 1)
                continue
        except:
            ''
        try:
            if reserve.index(i + 1) >= 0:
                answer += 1
                reserve.remove(i + 1)
                continue
        except:
            ''

    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [1, 2], [2, 3]))
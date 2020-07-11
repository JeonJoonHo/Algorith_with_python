# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3

def solution(N, number):
    answer = 0

    arr = [set() for i in range(8)]

    for i, num in enumerate(arr, start=1):
        num.add(int(str(N) * i))

    for i in range(1, 8):
        if number in arr[i - 1]:
            answer = i
            break

        for j in range(i):
            for value1 in arr[j]:
                for value2 in arr[i - j - 1]:
                    arr[i].add(value1 + value2)
                    arr[i].add(value1 - value2)
                    arr[i].add(value1 * value2)
                    if value2 != 0:
                        arr[i].add(value1 // value2)

        if number in arr[i]:
            answer = i + 1
            break

    if answer == 0:
        answer = -1

    return answer

print(solution(2, 99))
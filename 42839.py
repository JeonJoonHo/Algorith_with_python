# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

import math

def prime_list(n):
    primes = [True] * n

    max = int(math.sqrt(n))
    for i in range(2, (max + 1)):
        if primes[i]:
            for j in range(i+i, n, i):
                primes[j] = False

    return [number for number in range(2, n) if primes[number]]

def solution(numbers):
    answer = 0

    list_for_calculate_max = list(numbers)
    list_for_calculate_max.sort(reverse=True)

    max = int(''.join(list_for_calculate_max))

    for number in prime_list(max + 1):
        include = True

        check_numbers_list = list(numbers)
        for value in list(str(number)):
            if value not in check_numbers_list:
                include = False
                break

            check_numbers_list.remove(value)

        if include:
            answer += 1

    return answer

print(solution('17'))

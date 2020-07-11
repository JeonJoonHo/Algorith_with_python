# https://programmers.co.kr/learn/courses/30/lessons/42841?language=python3

import itertools

def solution(baseball):
    pool = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    numbers = list(map(''.join, itertools.permutations(pool, 3)))

    for answer in baseball:
        expect_numbers = []

        answer_number, expect_strike, expect_ball = answer
        answer_number_list = list(str(answer_number))

        for number in numbers:
            number_list = list(number)
            strike, ball = 0, 0
            for i, i_value in enumerate(number_list):
                for j, j_value in enumerate(answer_number_list):
                    if i_value == j_value and i == j:
                        strike += 1
                    elif i_value == j_value:
                        ball += 1

            if expect_strike == strike and expect_ball == ball:
                expect_numbers.append(number)

        numbers = expect_numbers

    return len(numbers)

print(solution([[523, 1, 0], [856, 0, 1], [934, 0, 1], [146, 1, 0]]))

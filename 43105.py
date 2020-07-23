# https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
import copy
def solution(triangle):
    length = len(triangle)
    sum_dp = copy.deepcopy(triangle)

    sum_dp[0] = triangle[0]
    for index in range(length-1):
        next_value = triangle[index + 1]

        for i, v in enumerate(sum_dp[index]):
            for add in range(2):
                current_idx = i + add
                if current_idx > len(next_value):
                    continue

                sum_value = v + next_value[current_idx]
                if sum_dp[index+1][current_idx] < sum_value:
                    sum_dp[index+1][current_idx] = sum_value

    return max(sum_dp[length-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))
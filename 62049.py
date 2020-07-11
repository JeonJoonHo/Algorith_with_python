# https://programmers.co.kr/learn/courses/30/lessons/62049?language=python3

def solution(n):
    dp = [0] * 21
    dp[1] = [0]
    dp[2] = [0, 0, 1]

    for value in range(3, n + 1):
        dp[value] = dp[value - 1] + [0] + list(map(lambda x: 1 if x == 0 else 0, dp[value - 1][::-1]))

    return dp[n]

print(solution(1))
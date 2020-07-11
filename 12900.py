# https://programmers.co.kr/learn/courses/30/lessons/12900?language=python3

def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] = dp[i] % 1000000007

    return dp[n]

print(solution(60000))
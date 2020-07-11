# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3
def solution(prices):
    answer = []

    prices_size = len(prices)
    for i in range(prices_size):
        current_index = i + 1
        while current_index < prices_size:
            if current_index == (prices_size - 1):
                answer.append(current_index - i)
                break

            if prices[current_index] < prices[i]:
                answer.append(current_index - i)
                break

            current_index += 1

    answer.append(0)
    return answer

print(solution([1, 2, 3, 2, 3]))
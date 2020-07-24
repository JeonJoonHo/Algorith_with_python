# https://programmers.co.kr/learn/courses/30/lessons/43237?language=python3

def find_target_index(budgets, left, right, ceiling):
    mid = int((right + left) / 2)

    if budgets[mid] < ceiling:
        if mid+1 >= right:
            return mid+1
        return find_target_index(budgets, mid, right, ceiling)
    elif budgets[mid] > ceiling:
        if left >= mid:
            return mid
        return find_target_index(budgets, left, mid, ceiling)

def solution(budgets, M):
    budgets.sort()

    current_total_budgets = sum(budgets)
    if M > current_total_budgets:
        return budgets[-1]

    length_ceiling_target = len(budgets)
    while True:
        ceiling = int(M / length_ceiling_target)
        index = find_target_index(budgets, 0, length_ceiling_target-1, ceiling)
        if index == 0:
            return ceiling

        M -= sum(budgets[0:index])
        budgets = budgets[index:length_ceiling_target]
        length_ceiling_target -= index

print(solution([30, 50, 140, 150, 130, 160], 511))
# print(solution([120, 110, 140, 150], 485))

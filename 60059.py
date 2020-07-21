# https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3
import copy

def rotate(table, M):
    rotate_table = [[1] * M for i in range(M)]
    for i in range(M):
        for j in range(M):
            rotate_table[i][j] = table[M-j-1][i]
    return rotate_table

def check(table, key, N, M, i, j):
    for k in range(M):
        for l in range(M):
            table[i + k][j + l] = table[i + k][j + l] + key[k][l]

    for k in range(M - 1, N + M - 1):
        for l in range(M - 1, N + M - 1):
            if table[k][l] != 1:
                return False

    return True

def solution(key, lock):
    answer = False

    N = len(lock)
    M = len(key)
    expend_lock_table = [[1] * (2*M+N-2) for i in range(2*M+N-2)]

    for i in range(M - 1, N + M - 1):
        for j in range(M - 1, N + M - 1):
            expend_lock_table[i][j] = lock[i - (M - 1)][j - (M - 1)]

    for _ in range(4):
        for i in range(N + 2):
            for j in range(N + 2):
                print(i, j)
                expend_lock_temp_table = copy.deepcopy(expend_lock_table)

                equal = check(expend_lock_temp_table, key, N, M, i, j)

                if equal == True:
                    return True

        key = rotate(key, M)

    return answer

print(solution([[1, 0, 1, 1], [1, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 0 ,0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

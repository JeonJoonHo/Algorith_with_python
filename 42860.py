# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def solution(name):
    alphabets = ['A', 'B', 'C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J' ,'K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U', 'V', 'W', 'X', 'Y' ,'Z']
    name_length = len(name)

    alphabet_count = 0
    movement_count = 0

    index = 0
    if name[index-1] == 'A':
        reverse = False
    else:
        reverse = True
    while index < name_length:
        if alphabets.index(name[index]) > 13:
            alphabet_index = 26 - alphabets.index(name[index])
        else:
            alphabet_index = alphabets.index(name[index])

        alphabet_count += alphabet_index

        index += 1

    index = 1
    while index < name_length:
        if reverse:
            if name[index] == 'A':
                movement_count += 1
            else:
                break

        else:
            if name[-index] == 'A':
                movement_count += 1
            else:
                break

        index += 1

    return alphabet_count + len(name) - 1 - movement_count

print(solution('JEROEN'))
print(solution('JAN'))
print(solution('JAZ'))
print(solution('ZZAAAAAAAAAAAAAZZ'))
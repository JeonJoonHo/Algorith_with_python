# https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3

def solution(arrangement):
    answer = 0# https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3


    arrangement = arrangement.replace('()', '1')

    brace_index = 0
    brace_array = []
    complete_brace_array = []

    for index, arrange in enumerate(arrangement):
        if arrange == '(':
            brace_array.append({'start_index': index, 'end_index': 0})
            brace_index += 1
            continue

        if arrange == ')':
            last_brace = brace_array.pop()
            last_brace['end_index'] = index
            complete_brace_array.append(last_brace)
            brace_index -= 1
            continue

    for complete_brace in complete_brace_array:
        start_index = complete_brace['start_index']
        end_index = complete_brace['end_index'] + 1
        answer += arrangement[start_index:end_index].count('1') + 1

    return answer

print(solution('()(((()())(())()))(())'))
# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

def solution(number, k):
    answer = [number[0]]

    for n in number[1:]:
        if k <= 0 :
            answer.append(n)
            continue

        answer.append(n)
        for i in range(1, len(answer)):
            if k <= 0:
                break
            if answer[-i-1] < n:
                k -= 1
                answer[-i-1] = '0'

        if '0' in answer:
            answer = list(filter(('0').__ne__, answer))

    return answer

# print(solution("1924", 2))
# print(solution("1231234", 3))
print(solution("4177252841", 4))
# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    length_citations = len(citations)

    for i in range(length_citations, 0, -1):
        h = i

        max_quotation = 0
        for citation in citations:
            if citation < h:
                break

            max_quotation += 1

        if max_quotation >= h and (length_citations - max_quotation) <= h:
            answer = h
            break

    return answer

print(solution([3, 0, 6, 1, 5]))

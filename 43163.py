# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

def solution(begin, target, words):
    check = set()

    level = {0: [begin]}
    for current_level in range(0, 50):
        new_level = set()
        for key in level[current_level]:
            for word in words:
                if key == word:
                    continue
                diff_count = 0

                for i in range(len(word)):
                    if key[i] != word[i]:
                        diff_count += 1
                    if diff_count > 1:
                        break

                if diff_count == 1:
                    new_level.add(word)

        current_level += 1
        level[current_level] = new_level - check
        check |= new_level

        if target in new_level:
            return current_level
        if len(new_level) == 0:
            return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

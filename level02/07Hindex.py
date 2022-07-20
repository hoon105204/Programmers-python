# https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    answer = 0
    array = [0]*10001
    for i in citations:
        array[i] += 1

    for i in range(10001):
        if i <= sum(array[i:]):
            answer = i
    return answer


def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution2([3, 3, 1, 0]))
# https://school.programmers.co.kr/learn/courses/30/lessons/42839
import itertools


def solution(numbers):
    answer = 0
    mylist = []
    for i in range(len(numbers)):
        mylist += list(map(''.join, itertools.permutations(numbers, i + 1)))

    mylist = list(set(map(int, mylist)))

    for i in mylist:
        if i in (2, 3, 5):
            answer += 1
        if i > 5 and i % 2 != 0:
            for j in range(3, i // 2, 2):
                if i % j == 0:
                    break
            else:
                answer += 1
    return answer


print(solution("17"))

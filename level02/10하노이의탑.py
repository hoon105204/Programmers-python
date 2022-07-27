# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def move(start, to):
    return [start, to]


def hanoi(n, start, to, via):
    if n == 1:
        return move(start, to)
    return hanoi(n-1, start, via, to) + move(start, to) + hanoi(n-1, via, to, start)


def solution(n):
    tmp = hanoi(n, 1, 3, 2)
    answer = []
    for i in range(0, len(tmp), 2):
        answer.append(tmp[i:i+2])

    return answer

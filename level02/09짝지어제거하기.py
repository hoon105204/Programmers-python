# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    answer = -1
    stack = []

    for i in s:
        if len(stack) >= 1 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        answer = 0
    else:
        answer = 1

    return answer


print(solution("doddod"))

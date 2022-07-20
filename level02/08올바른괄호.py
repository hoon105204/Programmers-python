# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    answer = True
    stack = []

    for val in s:
        stack.append(val)
        if len(stack) >= 2 and stack[-2:] == ["(",")"]:
            stack.pop()
            stack.pop()

    if stack:
        answer = False
    else:
        answer = True

    return answer
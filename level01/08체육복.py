# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s

    for i in sorted(r):
        if i-1 in l:
            l.remove(i-1)
        elif i+1 in l:
            l.remove(i+1)

    return n - len(l)

n = 5
lost = [1,2, 4]
reserve	= [1,3, 4,5]

print(solution(n, lost, reserve))

# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    tmp_list = [number[0]]

    for numb in number[1:]:
        while tmp_list and tmp_list[-1] < numb and k > 0:
            k -= 1
            tmp_list.pop()
        tmp_list.append(numb)

    if k != 0:
        tmp_list = tmp_list[:-k]

    return ''.join(tmp_list)


number = "131331131"
k = 4
print(solution(number, k))

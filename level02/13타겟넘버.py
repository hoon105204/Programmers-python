# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0
    arr = [0]
    arr2 = func1(arr, numbers, 0)

    for i in arr2:
        if i == target:
            answer += 1
    return answer


def func1(sum_list, numbers, start):
    res = []
    for j in range(len(sum_list)):
        res.append(sum_list[j] + numbers[start])
        res.append(sum_list[j] - numbers[start])
    if start == len(numbers)-1:
        return res

    return func1(res, numbers, start + 1)


print(solution([4, 1, 2, 1], 4))

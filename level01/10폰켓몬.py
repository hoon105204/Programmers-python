# https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    answer = 0
    my_dict = {}
    for val in nums:
        if my_dict.get(val) is None:
            my_dict[val] = 1
            answer += 1

    if answer > (len(nums)/2):
        answer = len(nums)/2

    return answer

print(solution([3,1,2,3]))

# 짧은 풀이
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))

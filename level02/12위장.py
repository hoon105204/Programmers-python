from collections import Counter


def solution(clothes):

    arr = Counter([ctype for _, ctype in clothes]).values()

    answer = 1
    for i in arr:
        answer *= i+1

    return answer - 1


# def solution(clothes):
#
#     my_dict = {}
#     for item in clothes:
#         item_type = item[1]
#         num = my_dict.get(item_type)
#         if num is None:
#             my_dict[item_type] = 1
#         else:
#             my_dict[item_type] += 1
#
#     answer = 1
#     for i in my_dict.values():
#         answer *= i+1
#
#     return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

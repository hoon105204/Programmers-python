# https://school.programmers.co.kr/learn/courses/30/lessons/64064
from itertools import *


def solution(user_id, banned_id):
    my_dict = []
    for ban_word in banned_id:
        tmp_list = []
        for user_word in user_id:
            if len(ban_word) == len(user_word):
                for i in range(len(ban_word)):
                    if ban_word[i] != "*" and ban_word[i] != user_word[i]:
                        break
                else:
                    tmp_list.append(user_word)
        my_dict.append(tmp_list)
    my_set = set()
    for tmp in list(product(*my_dict)):
        if len(tmp) == len(set(tmp)):
            my_set.add(tuple(list(sorted(tmp))))

    return len(my_set)


user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))

# https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


def solution(begin, target, words):
    distance = [-1]*(len(words) + 1)
    words = [begin] + words
    que = deque()
    que.append(words[0])
    distance[0] = 0


    while que:
        root_word = que.popleft()
        for i in range(len(words)):
            compare_word = words[i]
            # 방문했다면 스킵
            if distance[i] != -1:
                continue
            # 근처 단어가 아니면 스킵
            if not closeWord(compare_word, root_word):
                continue
            else:
                distance[i] = distance[words.index(root_word)] + 1
                que.append(compare_word)
            # 만약 근처단어에 target 단어라면
            if compare_word == target:
                return distance[i]

    return 0


def closeWord(word1, word2):
    word_list1 = list(word1)
    word_list2 = list(word2)
    answer = 0

    for i in range(len(word_list1)):
        if word_list1[i] != word_list2[i]:
            answer += 1

    if answer == 1:
        return True
    else:
        return False


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


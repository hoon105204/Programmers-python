# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# def solution(participant, completion):
#
#     participant.sort()
#     completion.sort()
#
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#
#     return participant[-1]

# import collections
#
#
# def solution(participant, completion):
#     # 카운터 객체는 서로 뺄 수 있음
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     print(collections.Counter(participant))
#     print(answer)
#     return list(answer.keys())[0]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
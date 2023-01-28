# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    user1 = [1,2,3,4,5]
    user2 = [2,1,2,3,2,4,2,5]
    user3 = [3,3,1,1,2,2,4,4,5,5]

    score = [0, 0, 0]
    name = [1,2,3]
    answer = []

    for i in range(len(answers)):
        x = i%len(user1)
        y = i%len(user2)
        z = i%len(user3)

        if user1[x] == answers[i]:
            score[0] += 1
        if user2[y] == answers[i]:
            score[1] += 1
        if user3[z] == answers[i]:
            score[2] += 1

    for i in range(3):
        if(max(score)==score[i]):
            answer.append(name[i])
    return answer

print(solution([1,3,2,4,2]))
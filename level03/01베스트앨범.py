# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    my_dict = {}
    my_dict2 = {}
    for i in range(len(genres)):
        tmp = my_dict.get(genres[i])
        if tmp is None:
            my_dict[genres[i]] = [(i, plays[i])]
        else:
            tmp.append((i, plays[i]))
            my_dict[genres[i]] = tmp

        tmp2 = my_dict2.get(genres[i])
        if tmp2 is None:
            my_dict2[genres[i]] = plays[i]
        else:
            my_dict2[genres[i]] += plays[i]

    arr = list(my_dict2.items())
    arr.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(arr)):
        gen = arr[i][0]
        for j in range(min(len(my_dict[gen]), 2)):
            my_dict[gen].sort(key=lambda x: x[1], reverse=True)
            answer.append(my_dict[gen][j][0])

    return answer


def solution2(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    genreSort = sorted(list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution2(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

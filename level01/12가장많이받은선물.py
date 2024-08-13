def solution(friends, gifts):
    answer = 0
    l_fr = len(friends)
    gift_score = [0] * l_fr
    gift_count = [0] * l_fr
    from_to = [[0] * l_fr for _ in range(l_fr)]
    idx = {friends[i]: i for i in range(l_fr)}

    for item in gifts:
        f, t = item.split()

        i = idx[f]
        j = idx[t]

        from_to[i][j] += 1
        gift_score[i] += 1
        gift_score[j] -= 1

    for i in range(l_fr):
        for j in range(l_fr):
            if from_to[i][j] > from_to[j][i]:
                gift_count[i] += 1
            elif from_to[i][j] == from_to[j][i] and gift_score[i] > gift_score[j]:
                gift_count[i] += 1

    answer = max(gift_count)

    return answer

friends, gifts = ["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]

print(solution(friends, gifts))

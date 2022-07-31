# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True

    set1 = set(phone_book)
    for val in phone_book:
        set2 = set()
        for i in range(len(val)):
            set2.add(val[0:i+1])
        set2.remove(val)

        if set1 & set2:
            return False

    return answer

print(solution(["12","123","1235","567","88"]))

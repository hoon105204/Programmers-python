# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

def solution(arr):
    answer = []

    if len(arr) == 0:
        return []
    else:
        tmp = 'A'
        for i in arr:
            if i != tmp:
                answer.append(i)
            tmp = i
    return answer

arr = [1,2,2,3,1,3,3,3,2,1,1]
print(solution(arr))



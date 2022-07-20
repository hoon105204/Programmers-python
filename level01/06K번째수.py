array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def k_num(array, command):
    new_array = array[command[0] - 1:command[1]]
    new_array.sort()

    return new_array[command[2] - 1]


def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(k_num(array, command))

    return answer

print(solution(array, commands))
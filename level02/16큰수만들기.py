# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    tmp_list = []
    answer = ""
    rest = ""
    forward = ""

    for i in range(len(number)):
        numb = int(number[i])

        if not tmp_list:
            tmp_list.append(numb)
            continue

        for j in range(len(tmp_list)):
            idx = len(tmp_list) - (j + 1)
            print("val: ", tmp_list[idx], ", numb: ", numb)

            if tmp_list[idx] >= numb:
                tmp_list.append(numb)
                break
            elif k != 0:
                tmp_list.pop()
                k -= 1
                continue
            else:
                print("do break!")
                break
        forward = ''.join(str(s) for s in tmp_list)
        print("[k: ", k,"], forward: ", forward, tmp_list, " number[:-i]: ",number[i:])
        if k != 0:
            answer = forward[:-k]
        else:
            answer = forward + number[:-i]
            break


    return answer


number = "123456789"
k = 3
print(solution(number, k))

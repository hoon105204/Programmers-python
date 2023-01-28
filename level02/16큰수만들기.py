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
        print("i: ", i)
        for j in range(len(tmp_list)):
            idx = len(tmp_list) - (j + 1)
            print("val: ", tmp_list[idx], ", numb: ", numb)

            if tmp_list[idx] >= numb:
                tmp_list.append(numb)
                break
            else:
                tmp_list.pop()
                k -= 1
                print("tmp_list: ", tmp_list, k)

            if k == 0:
                break

        forward = ''.join(str(s) for s in tmp_list)
        print("[k: ", k,"], forward: ", forward, tmp_list, " number[i:]: ",number[i:])
        if k != 0:
            answer = forward[:-k]
            print(k)
        else:
            answer = forward + number[i:]
            break

    return answer


number = "9146"
k = 2
print(solution(number, k))

number = "98876554321"
k = 6
print(solution(number, k))
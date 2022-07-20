# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):

    N = len(board[0])

    answer=0
    mystack = [0]

    for z in moves:
        i = z-1
        for j in range(N):
            if board[j][i] != 0:
                if mystack[-1] == board[j][i]:
                    answer += 1
                    mystack.pop()
                    board[j][i]=0
                    break
                else:
                    mystack.append(board[j][i])
                    board[j][i]=0
                    break

    return answer*2

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))

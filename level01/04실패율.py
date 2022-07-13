# def solution(N, stages):
#     answer = []
#     return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# result = [3,4,2,1,5]

# dodal = [0]*N       # 도달했던 갯수
# notclear = [0]*N    # 클리어하지 못한 갯수

# fail = []           # 실패율(클리어못한갯수/도달갯수)

# answer = []         # 정답(실패율 내림차순 인덱스)

# for i in stages:
    
#     if i != N+1:
#         notclear[i-1] += 1        # notclear  [1,2,0,0,0]
#         for j in range(i):        # dodal     [4,3,1,1,1]
#             dodal[j] += 1          
#     else:
#         for i in range(N):
#             dodal[i] += 1

# print('\ndodal={}'.format(dodal))
# print('notclear={}\n'.format(notclear))

# for i in range(N):
#     x = dodal[i]
#     y = notclear[i]
#     # print('{}/{}'.format(y,x))
#     fail.append([y/x,i+1])
    
# print('[fail]={}'.format(fail))

# fail.sort(key= lambda x:x[0], reverse=True)
# print('[fail.sort]={}'.format(fail))

# for i in fail:
#     answer.append(i[1])
    
# print(answer)


def solution(N,stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
        print(denominator, result)
    return sorted(result, key = lambda x : result[x], reverse=True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(5,stages))
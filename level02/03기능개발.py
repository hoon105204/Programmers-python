# 남은 일수 계산 함수
def days(no,speed):
    if (100-no)%speed!=0:
        return (100-no)//speed + 1
    else: 
        return (100-no)//speed


def solution(progresses, speeds):

    myTime = []

    stack = []
    answer = []

    for x,y in zip(progresses, speeds):
        myTime.append(days(x,y))
        
    # print('myTime={}\n'.format(myTime))
    # n=0
    for i in myTime:
        # n+=1
        if len(stack)==0:
            stack.append(i)
        elif i > max(stack):
            answer.append(len(stack))
            stack=[i]
        else:
            stack.append(i)
        # print('{}th stack={}'.format(n,stack))
        # print('{}th answer={}\n'.format(n,answer))
    else:
        if len(stack) != 0:
            answer.append(len(stack))

    return answer

progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))
    

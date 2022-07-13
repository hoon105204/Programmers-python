def solution(priorities, location):
    mylist=[]
    for i in range(len(priorities)):
        mylist.append((i,priorities[i]))
    print(mylist)
    
    answer = 0
    while True:
        
        max = 0
        for tup in mylist:
            if tup[1] > max:
                max = tup[1]

        if mylist[0][1] == max:
            answer += 1
            if mylist[0][0] == location:
                break
            mylist.pop(0)  
        else:
            mylist.append(mylist.pop(0))
        print(answer, mylist)
    return answer

priorities, location = [1, 1, 9, 1, 1, 1], 0    
print(solution(priorities, location))
    
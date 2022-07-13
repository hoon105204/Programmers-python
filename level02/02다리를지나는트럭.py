# 내가 작성한 방법1
def solution(bridge_length, weight, truck_weights):
    spoint = truck_weights
    mpoint = []
    tpoint = []
    answer = 0

    while True:
        answer += 1

        if  len(spoint)!=0:
            if sum(mpoint) + spoint[0] <= weight:
                mpoint.append(spoint.pop(0))
                tpoint.append(0)

        for i in range(len(tpoint)):
            tpoint[i] +=1

        if tpoint[0] == bridge_length:
            tpoint.pop(0)
            mpoint.pop(0)

        if len(spoint)==0 and len(mpoint)==0:
            break
    return answer+1

# bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]
# solution(bridge_length, weight, truck_weights)

# 나의 풀이2 stack 이용
def solution2(bridge_length, weight, truck_weights):
    
    bridge = [0]*bridge_length
    time = 0
    
    while True:
        
        time += 1
        # print(time)
        bridge.pop(0)
        if len(truck_weights)!=0:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        else:
            bridge.append(0)
        # print(bridge)
        if len(truck_weights)==0 and sum(bridge)==0:
            break

    return time

bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]
print(solution2(bridge_length, weight, truck_weights))

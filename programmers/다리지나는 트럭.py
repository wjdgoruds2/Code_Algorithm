def solution(bridge_length, weight, truck_weights):
    time=0
    len=[0]*bridge_length
    while len:
        time+=1
        len.pop(0)
        if truck_weights:
            if sum(len)+truck_weights[0] <= weight:
                len.append(truck_weights.pop(0))
            else:
                len.append(0)

    return time
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
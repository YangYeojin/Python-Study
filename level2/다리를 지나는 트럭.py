def solution(bridge_length, weight, truck_weights):
    seconds = 0
    queue = [0] * bridge_length
    sumQ = 0
    while truck_weights:
        seconds += 1
        sumQ -= queue[0]
        queue.pop(0)
        if truck_weights[0] + sumQ <= weight:
            sumQ += truck_weights[0]
            temp = truck_weights[0]
            truck_weights.pop(0)
            queue.append(temp)
        else:
            queue.append(0)
    return seconds + bridge_length

print(solution(5, 10, [7, 2, 3, 1, 8, 5]))
print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
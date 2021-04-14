# 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    onBridge = deque([0] * (bridge_length))
    sumOnBridge = 0

    while truck_weights:
        answer+=1
        outTruck = onBridge.popleft()
        sumOnBridge -= outTruck
        if sumOnBridge + truck_weights[0] <= weight:
            onBridge.append(truck_weights.popleft())
            sumOnBridge += onBridge[-1]
        else:
            onBridge.append(0)

    answer+=bridge_length

    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
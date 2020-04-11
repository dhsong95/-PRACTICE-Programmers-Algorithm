def solution(bridge_length, weight, truck_weights):
    current_time = 0
    current_weight = 0

    truck_in_bridge = list()

    for truck in truck_weights:
        if current_weight == 0:
            truck_in_bridge.append((truck, bridge_length))
            current_weight += truck
        else:
            top = truck_in_bridge[0]
            if (truck + current_weight) <= weight:
                current_time += 1
                for idx, item in enumerate(truck_in_bridge):
                    truck_in_bridge[idx] = (item[0], item[1] - 1)

                if truck_in_bridge[0][1] == 0:
                    current_weight -= top[0]
                    truck_in_bridge.pop(0)
            else:
                while truck_in_bridge and ((truck + current_weight) > weight):
                    top = truck_in_bridge.pop(0)
                    current_time += top[1]
                    for idx, item in enumerate(truck_in_bridge):
                        truck_in_bridge[idx] = (item[0], item[1] - top[1])
                    current_weight -= top[0]

            truck_in_bridge.append((truck, bridge_length))
            current_weight += truck
    return current_time + bridge_length + 1


assert solution(2, 10, [7, 4, 5, 6]) == 8
assert solution(100, 100, [10]) == 101
assert solution(5, 12, [5, 4, 3, 2, 3, 2, 2]) == 14

from collections import deque


# queue 에 있는 트럭을 distance 만큼 이동시킨다. (pop -> 변환 -> push)
# distance 만큼 이동시켰을때 다리를 벗어나는 트럭에 대한 처리 필요 (bridge_weight 감소)
def move_trucks(queue, distance, bridge_weight):
    length = len(queue)
    for _ in range(length):
        w, d = queue.popleft()
        # distance 만큼 이동시켰을때 다리를 벗어나지 않는 트럭에 대해서만 push 수행
        if d - distance > 0:
            queue.append((w, d - distance))
        else:
            bridge_weight -= w

    return bridge_weight


def solution(bridge_length, weight, truck_weights):
    queue = deque([])   # 다리 역할은 큐로 구현한다
    time = 0            # 경과 시간
    bridge_weight = 0   # 다리에 있는 트럭의 무게 합

    for truck_weight in truck_weights:
        # 현재 트럭이 다리에 진입할 수 있는 경우
        if bridge_weight + truck_weight <= weight:
            # 트럭 이동과 그에 따른 다리에 있는 트럭 무게 변화 && 시간 경과
            bridge_weight = move_trucks(queue, 1, bridge_weight)
            time += 1

            # 트럭 다리 진입과 그에 따른 다리에 있는 트럭 무게 변화
            queue.append((truck_weight, bridge_length))
            bridge_weight += truck_weight

        # 현재 트럭이 다리에 진입할 수 없는 경우
        else:
            # 현재 트럭이 다리에 진입할 수 있을때까지 반복
            while queue:
                # 이동거리가 가장 짧은 트럭 다리 벗어나고 그에 따른 다리에 있는 트럭 무게 변화 && 시간 경과
                w, d = queue.popleft()
                bridge_weight -= w
                bridge_weight = move_trucks(queue, d, bridge_weight)
                time += d

                if bridge_weight + truck_weight <= weight:
                    break

            # 트럭 다리 진입과 그에 따른 다리에 있는 트럭 무게 변화
            queue.append((truck_weight, bridge_length))
            bridge_weight += truck_weight

    # 다리에 가장 마지막에 위치한 트럭이 다리를 빠져나오는 시간만큼 시간 추가
    last_w, last_d = queue.pop()
    time += last_d

    return time


if __name__ == '__main__':
    assert solution(2, 10, [7, 4, 5, 6]) == 8
    assert solution(100, 100, [10]) == 101
    assert solution(5, 12, [5, 4, 3, 2, 3, 2, 2]) == 14

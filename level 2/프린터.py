from collections import deque


def solution(priorities, location):
    queue = deque(priorities)
    counter = 0

    while queue:
        max_priority = max(queue)
        priority = queue.popleft()

        if priority == max_priority:
            counter += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            queue.append(priority)
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1

    return counter


if __name__ == '__main__':
    assert solution([2, 1, 3, 2], 2) == 1

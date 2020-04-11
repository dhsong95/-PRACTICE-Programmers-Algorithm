def solution(priorities, location):
    move = 0
    while priorities:
        max_priority = max(priorities)
        top_priority = priorities.pop(0)

        if top_priority == max_priority:
            move += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(top_priority)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    return move


try:
    assert solution([2, 1, 3, 2], 2) == 1
except AssertionError:
    print(solution([2, 1, 3, 2], 2))

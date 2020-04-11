def solution(progresses, speeds):
    left_progresses = [((100 - progress) // speeds[idx]) + (1 if (100 - progress) % speeds[idx] else 0)
                       for idx, progress in enumerate(progresses)]

    work = list()
    while left_progresses:
        pop = left_progresses.pop(0)
        consecutive = 1
        while left_progresses and pop >= left_progresses[0]:
            left_progresses.pop(0)
            consecutive += 1
        work.append(consecutive)
    return work


assert solution([93,30,55], [1,30,5]) == [2, 1]

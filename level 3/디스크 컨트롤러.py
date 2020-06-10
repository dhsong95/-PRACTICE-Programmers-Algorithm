import heapq


def solution(jobs):
    # 전체 작업을 관리하는 최소 힙 (요청 시간, 소요 시간)
    heap = list()
    for start, duration in jobs:
        heapq.heappush(heap, (start, duration))

    # 현재 시간
    current_time = 0
    # 모든 작업의 요청부터 처리까지 걸리 시간의 합
    process_time = 0

    # 대기 작업을 관리하는 최소 힙. (소요 시간, 요청 시간)
    waiting_heap = list()

    # 전체 작업을 관리하는 힙 또는 대기 작업으 과리하는 힙에 작업이 남아있는 경우
    while heap or waiting_heap:

        # 대기 작업 선별
        while heap and heap[0][0] <= current_time:
            start, duration = heapq.heappop(heap)
            heapq.heappush(waiting_heap, (duration, start))

        # 대기 작업이 있는 경우 최적의 작업을 선택. 최적의 작업 == 소요 시간이 가장 짧은 작업
        if waiting_heap:
            duration, start = heapq.heappop(waiting_heap)
            # 작업 처리 시간 + 대기 시간(현재 시간 - 요청 시간)
            process_time += (duration + (current_time - start))
            current_time += duration
        # 대기 작업이 없는 경우에는 현재 시간은 전체 작업 중 가장 빠른 요청이 들어오는 시간으로 바꾼다.
        else:
            current_time = heap[0][0]

    # 평균을 구한다
    return process_time // len(jobs)


if __name__ == '__main__':
    assert solution([[0, 3], [1, 9], [2, 6]]) == 9
    assert solution([[0, 3], [4, 3], [10, 3]]) == 3
    assert solution([[0, 10], [2, 3], [9, 3]]) == 9
    assert solution([[1, 10], [3, 3], [10, 3]]) == 9
    assert solution([[0, 10]]) == 10
    assert solution([[0, 10], [4, 10], [5, 11], [15, 2]]) == 15

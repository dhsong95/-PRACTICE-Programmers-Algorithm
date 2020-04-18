import heapq


def solution(scoville, K):
    heap = list()
    for s in scoville:
        heapq.heappush(heap, s)

    counter = 0
    while len(heap) > 1 and heap[0] < K:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        new_s = first + 2 * second
        heapq.heappush(heap, new_s)
        counter += 1

    return counter if heap[0] >= K else -1


if __name__ == '__main__':
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2


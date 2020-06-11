import heapq


def solution(operations):
    # 숫자를 관리할 최소 힙 (min heap)
    heap = list()

    for operation in operations:
        # heap push
        if operation[0] == 'I':
            num = int(operation[2:])
            heapq.heappush(heap, num)
        # heap pop
        elif operation == 'D -1':
            if heap:
                heapq.heappop(heap)
        # 최대값을 찾아서 리스트에서 제거
        elif operation == 'D 1':
            if heap:
                heap.remove(max(heap))

    return [max(heap), heap[0]] if heap else [0, 0]


if __name__ == '__main__':
    assert solution(["I 16", "D 1"]) == [0, 0]
    assert solution(["I 7", "I 5", "I -5", "D -1"]) == [7, 5]
    assert solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]) == [0, 0]
    assert solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]) == [333, -45]
    assert solution(["I 1", "I 2", "I 3", "I 4", "I 5",
                     "I 6", "I 7", "I 8", "I 9", "I 10",
                     "D 1", "D -1", "D 1", "D -1", "I 1",
                     "I 2", "I 3", "I 4", "I 5", "I 6",
                     "I 7", "I 8", "I 9", "I 10", "D 1",
                     "D -1", "D 1", "D -1"]) == [8, 3]
    assert solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]) == [6, 5]
    assert solution(["I 2", "I 2", "I 3", "D -1", "D 1", "D 1"]) == [0, 0]

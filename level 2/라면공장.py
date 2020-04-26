import heapq


def solution(stock, dates, supplies, k):
    heap = list()
    duration = stock
    counter = 0
    idx = 0
    while duration < k:
        while idx < len(dates) and dates[idx] <= duration:
            heapq.heappush(heap, -supplies[idx])
            idx += 1
        duration -= heapq.heappop(heap)
        counter += 1
    return counter


if __name__ == '__main__':
    assert solution(4, [4, 10, 15], [20, 5, 10], 30) == 2

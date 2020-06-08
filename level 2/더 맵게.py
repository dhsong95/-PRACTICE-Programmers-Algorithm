import heapq


def solution(scoville, K):
    # scoville을 힙 자료구조로 초기화
    heap = list()
    for s in scoville:
        heapq.heappush(heap, s)

    counter = 0

    # 가장 작은 스코빌 지수
    s1 = heapq.heappop(heap)
    while s1 < K:
        if not heap:
            return -1

        # 그 다음으로 작은 스코빌 지수
        s2 = heapq.heappop(heap)
        # 섞은 스코빌 지수
        s3 = s1 + 2 * s2
        counter += 1

        # 섞은 스코빌 지수를 다시 힙에 원소로 넣는다
        heapq.heappush(heap, s3)

        s1 = heapq.heappop(heap)

    return counter


if __name__ == '__main__':
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2


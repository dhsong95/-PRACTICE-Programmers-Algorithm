import heapq


def solution(stock, dates, supplies, k):
    # 최대 힙을 위한 힙
    heap = list()

    # 인덱스: 현재 재고량으로 버틸 수 있는 일수를 가리킨다
    idx = 0

    # 공급 횟수 카운터
    counter = 0

    # 현재 재고량으로 목표치를 버틸 수 없는 경우
    while stock < k:
        # 현재 재고량으로 버틸 수 있는 일수의 공급량을 모두 힙에 저장
        # 최대 힙으로 구현해야하므로 -1 이 곱해진다
        while idx < len(dates) and dates[idx] <= stock:
            heapq.heappush(heap, -supplies[idx])
            idx += 1

        # -1이 곱해져서 원래의 공급량으로 복원
        supply = -1 * heapq.heappop(heap)

        # 재고량에 공급량 반영
        stock += supply

        # 공급 횟수 증가
        counter += 1

    return counter


if __name__ == '__main__':
    assert solution(4, [4, 10, 15], [20, 5, 10], 30) == 2
    assert solution(4, [1, 2, 3, 4], [1, 1, 1, 1], 6) == 2

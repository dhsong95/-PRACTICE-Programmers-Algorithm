def solution(citations):
    # 인용 횟수를 오름차순으로 정렬
    citations = sorted(citations)
    # 전체 논문의 수
    n = len(citations)
    # H Index 초기값은 0이다. 일단 논문이 제출되면 0 번 인용 횟수를 가진 논문은 0개 이상이다.
    h_index = 0
    for idx, citation in enumerate(citations):
        # i 번째 인용 횟수가 남은 논문의 수보다 많은 지점에서 최대 H Index 가 결정된다
        if citation >= (n - idx):
            h_index = (n - idx)
            break

    return h_index


if __name__ == '__main__':
    assert solution([3, 0, 6, 1, 5]) == 3
    assert solution([6, 6, 6, 6, 6]) == 5

def solution(prices):
    stack = [(prices[-1], 0)]
    times = [0]

    # prices 를 역순으로 순회하기 위한 인덱스
    idx = len(prices) - 2
    time = 1

    while idx >= 0:
        price = prices[idx]
        # 주가 유지 시간이 결정된 경우
        if (not stack) or (stack and price > stack[-1][0]):
            # 정보 저장
            stack.append((price, time))
            times.append(time)

            # 다음 주식 정보를 가리키고 보유 시간을 1로 초기화
            idx -= 1
            time = 1
        # 현재 시점을 기준으로 다음 시점까지의 주가가 떨어지지 않았으므로 주가 유지 시간을 더한다
        else:
            _, t = stack.pop(-1)
            time += t

    # 유지 시간의 역순을 출력
    return times[::-1]


if __name__ == '__main__':
    assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]
    assert solution([1, 4, 4, 3, 4]) == [4, 2, 1, 1, 0]

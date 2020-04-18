def solution(n):
    folded = [0]
    for _ in range(1, n):
        folded = folded + [0] + [0 if f == 1 else 1 for f in folded[::-1]]
    return folded


if __name__ == '__main__':
    assert solution(1) == [0]
    assert solution(2) == [0, 0, 1]
    assert solution(3) == [0, 0, 1, 0, 0, 1, 1]

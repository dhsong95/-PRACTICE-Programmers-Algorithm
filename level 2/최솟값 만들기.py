def solution(A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    return sum([a * b for a, b in zip(A, B)])


if __name__ == '__main__':
    assert solution([1, 4, 2], [5, 4, 4]) == 29
    assert solution([1, 2], [3, 4]) == 10
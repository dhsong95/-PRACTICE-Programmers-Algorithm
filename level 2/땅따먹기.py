def solution(land):
    n_row = len(land)
    n_col = len(land[0])

    score = [[0] * n_col for _ in range(n_row)]
    score[0] = land[0]

    for rdx in range(1, n_row):
        for cdx in range(n_col):
            score[rdx][cdx] = max(score[rdx - 1][:cdx] + score[rdx - 1][cdx + 1:]) + land[rdx][cdx]

    return max(score[-1])


if __name__ == '__main__':
    assert solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]) == 16


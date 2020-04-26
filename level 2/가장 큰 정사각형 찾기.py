def solution(board):
    square = [[0] * len(board[0]) for _ in range(len(board))]
    square[0] = board[0]

    width = 0 if sum(sum(board, [])) == 0 else 1

    for rdx in range(1, len(board)):
        square[rdx][0] = board[rdx][0]
        for cdx in range(1, len(board[0])):
            w = (min(square[rdx - 1][cdx - 1], square[rdx][cdx - 1], square[rdx - 1][cdx]) + 1) * board[rdx][cdx]
            square[rdx][cdx] = w
            width = w if w > width else width

    return width * width


if __name__ == '__main__':
    assert solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]) == 9
    assert solution([[0, 0, 1, 1], [1, 1, 1, 1]]) == 4
    assert solution([[0, 0, 1, 1]]) == 1
    assert solution([[0, 0, 0, 0]]) == 0
    assert solution([[0], [0], [1], [1]]) == 1
    assert solution([[0], [0], [0], [0]]) == 0
    assert solution([[0]]) == 0
    assert solution([[1]]) == 1

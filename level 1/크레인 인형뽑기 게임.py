def solution(board, moves):
    st = list()
    removed = 0
    for move in moves:
        target = None
        for row in board:
            if row[move - 1]:
                target = row[move - 1]
                row[move - 1] = 0
                break
        if st and target == st[-1]:
            st.pop(-1)
            removed += 2
        elif target:
            st.append(target)
    return removed


# Test Case
board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

assert solution(board, moves) == 4

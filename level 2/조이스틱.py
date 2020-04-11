def solution(name):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    up_down_move = list()
    for char in name:
        loc = alphabet.find(char)
        loc = len(alphabet) - loc if loc > 13 else loc
        up_down_move.append(loc)

    total_move = 0
    idx = 0
    while True:
        total_move += up_down_move[idx]
        up_down_move[idx] = 0

        if sum(up_down_move) == 0:
            break

        ldx = rdx = 1

        while up_down_move[idx - ldx] == 0:
            ldx += 1
        while up_down_move[idx + rdx] == 0:
            rdx += 1

        if ldx < rdx:
            total_move += ldx
            idx -= ldx
        else:
            total_move += rdx
            idx += rdx

    return total_move


assert solution('JEROEN') == 56

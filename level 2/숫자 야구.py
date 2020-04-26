import itertools


def solution(baseball):
    candidates = list(itertools.permutations(range(1, 10), 3))

    for trial, strike, ball in baseball:
        idx = 0
        trial = [int(char) for char in str(trial)]
        while idx < len(candidates):
            candidate = list(candidates[idx])

            s = 0
            b = 0

            for jdx in range(3):
                if candidate[jdx] == trial[jdx]:
                    s += 1
                elif trial[jdx] in candidate:
                    b += 1

            if s == strike and b == ball:
                idx += 1
            else:
                candidates.pop(idx)

    return len(candidates)


if __name__ == '__main__':
    assert solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]) == 2

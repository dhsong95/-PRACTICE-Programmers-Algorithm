def solution(brown, red):
    h = red
    v = 1
    candidates = [(h, v)]

    while v < int(red ** 0.5) + 1:
        if red % v == 0:
            h = red // v
            candidates.append((h, v))
        v += 1

    for h, v in candidates:
        if ((h + 2) * (v + 2) - h * v) == brown:
            return [h + 2, v + 2]


if __name__ == '__main__':
    assert solution(10, 2) == [4, 3]
    assert solution(8, 1) == [3, 3]
    assert solution(24, 24) == [8, 6]
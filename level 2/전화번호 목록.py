import itertools


def solution(phone_book):
    combinations = itertools.combinations(phone_book, 2)
    for combination in combinations:
        (short, long) = combination if len(combination[0]) < len(combination[1]) else combination[::-1]
        if long.startswith(short):
            return False
    return True


if __name__ == '__main__':
    assert not solution(['119', '97674223', '1195524421'])
    assert solution(['123', '456', '789'])
    assert not solution(['12', '123', '1235', '567', '88'])

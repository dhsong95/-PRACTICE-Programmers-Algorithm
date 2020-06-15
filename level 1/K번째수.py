def solution(array, commands):
    # 슬라이싱(start - 1 to end) -> 정렬(sorted function) -> 인덱싱(idx)
    return [sorted(array[start - 1: end])[idx - 1] for start, end, idx in commands]


if __name__ == '__main__':
    assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]
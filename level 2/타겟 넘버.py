def dfs(numbers, idx, source, target):
    if idx == len(numbers):
        return int(source == target)

    counter = 0

    counter += dfs(numbers, idx + 1, source + numbers[idx], target)
    counter += dfs(numbers, idx + 1, source - numbers[idx], target)

    return counter


def solution(numbers, target):
    counter = dfs(numbers, 0, 0, target)
    return counter


if __name__ == '__main__':
    assert solution([1, 1, 1, 1, 1], 3) == 5

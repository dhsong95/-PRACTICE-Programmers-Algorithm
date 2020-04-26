def solution(nums):
    return len(set(nums)) if len(set(nums)) < len(nums) // 2 else len(nums) // 2


if __name__ == '__main__':
    assert solution([3, 1, 2, 3]) == 2
    assert solution([3, 3, 3, 2, 2, 4]) == 3
    assert solution([3, 3, 3, 2, 2, 2]) == 2

def solution(s):
    nums = sorted([int(num) for num in s.split()])
    return ' '.join([str(nums[0]), str(nums[-1])])


if __name__ == '__main__':
    assert solution('1 2 3 4') == '1 4'
    assert solution('-1 -2 -3 -4') == '-4 -1'
    assert solution('-1 -1') == '-1 -1'


def solution(s):
    stack = list()
    for char in s:
        if char == '(':
            stack.append(char)
        elif stack:
            stack.pop(-1)
        else:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    assert solution('()()')
    assert solution('(())()')
    assert not solution(')()(')
    assert not solution('(()(')
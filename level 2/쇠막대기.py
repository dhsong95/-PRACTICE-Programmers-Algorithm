def solution(arrangement):
    idx = 0
    stack = list()
    counter = 0
    while idx < len(arrangement):
        # () 패턴: 레이저 동작
        if idx < len(arrangement) - 1 and arrangement[idx:idx + 2] == '()':
            counter += len(stack)
            idx += 2
        # ( 패턴: 쇠막대기 추가
        elif arrangement[idx] == '(':
            stack.append(arrangement[idx])
            idx += 1
        # ) 패턴: 마지막 쇠막대기 처리 필요
        elif arrangement[idx] == ')':
            stack.pop(-1)
            counter += 1
            idx += 1

    return counter


if __name__ == '__main__':
    assert solution('()(((()())(())()))(())') == 17

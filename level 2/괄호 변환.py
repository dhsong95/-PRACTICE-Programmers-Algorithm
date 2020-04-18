def valid_parenthesis(parenthesis):
    stack = list()
    idx = 0
    while idx < len(parenthesis):
        p = parenthesis[idx]
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop(-1)
        idx += 1
    return False if stack else True


def solution(p):
    if not p:
        return p

    counter_open = 0
    counter_close = 0
    idx = 0

    while idx < len(p) and ((counter_open == 0 and counter_close == 0) or (counter_open != counter_close)):
        counter_open += (1 if p[idx] == '(' else 0)
        counter_close += (1 if p[idx] == ')' else 0)
        idx += 1

    u = p[:idx]
    v = p[idx:]

    if valid_parenthesis(u):
        return u + solution(v)
    else:
        answer = ''
        answer += '('
        answer += solution(v)
        answer += ')'
        answer += ''.join([')' if p == '(' else '(' for p in u[1:-1]])
        return answer


if __name__ == '__main__':
    assert solution("(()())()") == "(()())()"
    assert solution(")(") == "()"
    assert solution("()))((()") == "()(())()"

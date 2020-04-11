def solution(arrangement):
    st = list()
    idx = 0
    total = 0
    while idx < len(arrangement):
        parenthesis = arrangement[idx]

        if parenthesis == '(':
            if idx + 1 < len(arrangement) and arrangement[idx + 1] == ')':
                total += len(st)
                idx += 1
            else:
                st.append(parenthesis)
        else:
            total += 1
            st.pop(-1)
        idx += 1
    return total


assert solution('()(((()())(())()))(())') == 17

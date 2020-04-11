def solution(prices):
    times = list()
    st = list()
    for price in prices[::-1]:
        time = 1 if st else 0

        while st and st[-1][0] >= price:
            top = st.pop(-1)
            time += top[1]

        times.append(time)
        st.append((price, time))
    return times[::-1]


assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]
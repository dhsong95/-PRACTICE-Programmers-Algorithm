def solution(heights):
    locations = [0] * len(heights)
    st = list()
    for idx in range(len(heights) - 1, -1, -1):
        while st and st[-1][1] < heights[idx]:
            top = st.pop(-1)
            locations[top[0]] = idx + 1
        st.append((idx, heights[idx]))
    return locations


assert solution([6, 9, 5, 7, 4]) == [0, 0, 2, 2, 4]

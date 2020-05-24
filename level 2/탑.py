def solution(heights):
    receiver = [0] * len(heights)
    stack = list()
    for idx in range(len(heights) - 1, -1, -1):
        idx_one = idx + 1
        height = heights[idx]
        while stack and height > stack[-1][0]:
            top_height, top_idx = stack.pop(-1)
            receiver[top_idx] = idx_one

        stack.append((height, idx))

    return receiver


assert solution([6, 9, 5, 7, 4]) == [0, 0, 2, 2, 4]

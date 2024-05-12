# Given an array of N  integers arr[] representing a height map (can be
# negative) where the width of each bar is 1,
# compute how much water it is able to trap after raining.
def trap_rain_water(heights):
    n = len(heights)
    if n < 3:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    trapped_water = 0
    for i in range(n):
        trapped_water += max(min(left_max[i], right_max[i]) - heights[i], 0)

    return trapped_water


# Example usage:
heights = [0, -1, -2, 5, 0, 4]
print(trap_rain_water(heights))  # outputs 7

# Time: O(n)
# Space: O(n)

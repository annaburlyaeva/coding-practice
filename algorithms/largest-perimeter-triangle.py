# Given an integer array nums, return the largest perimeter of a triangle
# with a non-zero area, formed from three of these lengths.
# If it is impossible to form any triangle of a non-zero area, return 0.
import heapq


def largest_perimeter(nums: list[int]) -> int:
    nums.sort(reverse=True)
    for i in range(3, len(nums) + 1):
        if nums[i - 3] < nums[i - 2] + nums[i - 1]:
            return sum(nums[i - 3:i])
    return 0


# Time: O(nlogn)
# Space: O(1)

def largest_perimeter(nums: list[int]) -> int:
    for i in range(len(nums)):
        nums[i] = -nums[i]
    nums.append(0)  # If we reach 0 then no solution
    heapq.heapify(nums)
    s1 = heapq.heappop(nums)
    s2 = heapq.heappop(nums)
    s3 = heapq.heappop(nums)
    while s3 and s1 <= s2 + s3:  # '<=' because every number is negative
        s1, s2, s3 = s2, s3, heapq.heappop(nums)
    if s3:
        return -(s1 + s2 + s3)
    return 0  # No solution

# Time: on average O(n), worst case O(nlogn)
# Space: O(1)

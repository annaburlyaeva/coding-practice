# Given a binary array nums and an integer goal,
# return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.
from collections import defaultdict


def num_subarrays_with_sum(nums: list[int], goal: int) -> int:
    res = defaultdict(int)
    res[0] = 1
    ans = 0
    prefix_sum = 0
    for i in nums:
        prefix_sum += i
        ans += res[prefix_sum - goal]
        res[prefix_sum] += 1
    return ans


# Time: O(n)
# Space: O(n)


def num_subarrays_with_sum(nums: list[int], goal: int) -> int:
    def sliding_window_at_most(nums: list[int], goal: int) -> int:
        start, current_sum, total_count = 0, 0, 0
        # Iterate through the array using a sliding window approach
        for end in range(len(nums)):
            current_sum += nums[end]
            # Adjust the window by moving the start pointer to the right
            # until the sum becomes less than or equal to the goal
            while start <= end and current_sum > goal:
                current_sum -= nums[start]
                start += 1
            # Update the total count by adding the length of the current subarray
            total_count += end - start + 1
        return total_count

    return sliding_window_at_most(nums, goal) - \
           sliding_window_at_most(nums, goal - 1)

# Time: O(n)
# Space: O(1)

# The median is the middle value in an ordered integer list.
# If the size of the list is even, there is no middle value.
# So the median is the mean of the two middle values.
# You are given an integer array nums and an integer k.
# There is a sliding window of size k
# which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
# Return the median array for each window in the original array.

import heapq


def sliding_window_median(nums, k):
    def add(num, small, large):
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
        else:
            heapq.heappush(large, num)
        balance(small, large)

    def remove(num, small, large):
        if num <= -small[0]:
            small.remove(-num)
            heapq.heapify(small)
        else:
            large.remove(num)
            heapq.heapify(large)
        balance(small, large)

    def balance(small, large):
        if len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        elif len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))

    def find_median(small, large):
        if len(small) > len(large):
            return -small[0]
        return (-small[0] + large[0]) / 2

    small, large = [], []
    result = []

    for i in range(len(nums)):
        add(nums[i], small, large)
        if i >= k - 1:
            result.append(find_median(small, large))
            remove(nums[i - k + 1], small, large)

    return result

# Time:
# Space:


# Given an integer array nums and an integer k,
# return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order,
# not the kth distinct element.
import heapq


def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
    return heap[0]


# Time: O(nlogk)
# Space: O(k)

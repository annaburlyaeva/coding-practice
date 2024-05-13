# Given a sorted array, find how many times integer target appears in the array.

def first_occurrence(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target and (mid == 0 or arr[mid - 1] < target):
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def last_occurrence(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target and (
                mid == len(arr) - 1 or arr[mid + 1] > target):
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def count_occurrences(arr: list[int], target: int) -> int:
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1

# Time: O(log(n))
# Space: O(1)

# There are n people that are split into some unknown number of groups.
# Each person is labeled with a unique ID from 0 to n - 1.
# You are given an integer array groupSizes,
# where group_sizes[i] is the size of the group that person i is in. ]For
# example, if group_sizes[1] = 3, then person 1 must be in a group of size 3.
# Return a list of groups such that
# each person i is in a group of size groupSizes[i].
# Each person should appear in exactly one group,
# and every person must be in a group.
# If there are multiple answers, return any of them.
# It is guaranteed that there will be at least one valid solution
# for the given input.

def group_people(group_sizes: list[int]) -> list[list[int]]:
    groups = {}
    res = []
    for i, size in enumerate(group_sizes):
        if size not in groups:
            groups[size] = []
        groups[size].append(i)
        if len(groups[size]) == size:
            res.append(groups[size])
            groups[size] = []
    return res

# Time: O(n)
# Space: O(n)

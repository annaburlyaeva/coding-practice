# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

def climb_stairs(n: int) -> int:
    memo = [0] * (n + 1)
    return climb(0, n, memo)


def climb(i: int, n: int, memo: list[int]) -> int:
    if i > n:
        return 0
    if i == n:
        return 1
    if memo[i] > 0:
        return memo[i]
    memo[i] = climb(i + 1, n, memo) + climb(i + 2, n, memo)
    return memo[i]

# Time: O(n)
# Space: O(n)

def climb_stairs(n):
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second

# Time: O(n)
# Space: O(1)
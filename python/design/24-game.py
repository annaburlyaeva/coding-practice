# Create a solver for 24 game

import math


def solve_24(nums: list[int]) -> bool:
    def generate(a: float, b: float) -> list[float]:
        return [a * b,
                a + b,
                a - b,
                b - a,
                math.inf if b == 0 else a / b,
                math.inf if a == 0 else b / a, ]

    def dfs(nums: list[float]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24.0) < 0.001
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for num in generate(nums[i], nums[j]):
                    nextRound = [num]
                    for k in range(len(nums)):
                        if k == i or k == j:
                            continue
                        nextRound.append(nums[k])
                    if dfs(nextRound):
                        return True

        return False

    return dfs(nums)


# Time: O(n^3 * 3^(n-1) * n! * (n-1)!)
# Space: O(n^2)


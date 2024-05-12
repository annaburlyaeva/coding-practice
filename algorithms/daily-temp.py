# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days
# you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible,
# keep answer[i] == 0 instead.

def daily_temp(t: list[int]) -> list[int]:
    n = len(t)
    max_temp = 0
    res = [0] * n
    # Iterate through the given array backwards
    for cur_day in range(n - 1, -1, -1):
        cur_temp = t[cur_day]
        if cur_temp >= max_temp:
            max_temp = cur_temp
            continue
        # Get the number of days until warmer temp
        days = 1
        while t[cur_day + days] <= cur_temp:
            # Use information from answer to search for the next warmer day
            days += res[cur_day + days]
        res[cur_day] = days
    return res

# Time: O(n)
# Space: O(1) extra, O(n) used to return the result

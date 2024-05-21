# Given array of numbers and limit,
# return a list of rows (comma separated strings)
# where length of each string is not greater than limit.
# Add trailing comma into each row except the last one.


def split_array_into_rows(arr, limit):
    rows = []
    current_row = ""
    for num in arr:
        if len(current_row) + len(str(num)) + 1 <= limit:
            if current_row:
                current_row += ","
            current_row += str(num)
        else:
            rows.append(current_row + ",")
            current_row = str(num)
    rows.append(current_row)
    return rows

# Time: O(n)
# Space: O(1) extra, O(n) total

# Given a string s containing
# just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Recursive approach
def is_valid(s: str) -> bool:
    open_to_close = {'(': ')', '[': ']', '{': '}'}

    def helper(s: str) -> bool:
        if s == "":
            return True
        for i in range(len(s)):
            if s[i] in open_to_close:
                if i + 1 < len(s) and s[i + 1] == open_to_close[s[i]]:
                    new_s = s[:i] + s[i + 2:]
                    return helper(new_s)

        return False

    return helper(s)


# Time: O(n)
# Space: O(n)

# Iterative approach
def is_valid(s: str) -> bool:
    open_to_close = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in s:
        if c not in open_to_close:
            if not stack or open_to_close[stack.pop()] != c:
                return False
        else:
            stack.append(c)
    return True if not stack else False

# Time: O(n)
# Space: O(n) (recursion stack)

# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid;
# there are no extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data
# does not contain any digits
# and that digits are only for those repeat numbers, k.
# For example, there will not be input like 3a or 2[4].


def decode_string(s: str) -> str:
    stack = []
    # Iterate through the string
    for char in s:
        # Add values to the stack until you reach "]"
        if char is not "]":
            stack.append(char)
        else:
            sub_str = ""
            # Get the most recent substring from the stack
            while stack[-1] is not "[":
                sub_str = stack.pop() + sub_str
            # Pop "["
            stack.pop()
            multiplier = ""
            # Get the multiplier
            while stack and stack[-1].isdigit():
                multiplier = stack.pop() + multiplier
            # Reuse stack add the multiplied substring
            stack.append(int(multiplier) * sub_str)
    return "".join(stack)

# Time: O(n)
# Space: O(n)

from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""

        def dfs(node):
            if not node:
                return "None,"

            result = str(node.val) + ","
            for child in node.children:
                result += dfs(child)
            result += "None,"  # Add a delimiter for the end of children
            return result

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None

        data = data.split(',')

        def dfs():
            if data[0] == "None":
                data.pop(0)
                return None

            node = Node(int(data[0]))
            data.pop(0)
            while data[0] != "None":
                node.children.append(dfs())
            data.pop(0)  # Remove the delimiter "None" for the end of children
            return node

        return dfs()


# Example usage:
# Create an N-ary tree
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

# Serialize the tree
ser = Codec()
serialized_tree = ser.serialize(root)
print("Serialized tree:", serialized_tree)

# Deserialize the tree
deserialized_tree = ser.deserialize(serialized_tree)


# Print the deserialized tree (for verification)
def print_tree(node):
    """Prints the tree with levels."""
    if not root:
        return

    queue = deque([(root, 0)])

    current_level = 0
    while queue:
        node, level = queue.popleft()

        if level != current_level:
            print()  # Move to the next line for the next level
            current_level = level

        print(node.val, end=" ")

        for child in node.children:
            queue.append((child, level + 1))


print("Deserialized tree:")
print_tree(deserialized_tree)

# Time: O(n)
# Space: O(n)

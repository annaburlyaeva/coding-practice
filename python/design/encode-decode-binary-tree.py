# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization
# algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string
# and this string can be deserialized to the original tree structure.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):

        def dfs(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = dfs(root.left, string)
                string = dfs(root.right, string)
            return string

        return dfs(root, '')

    def deserialize(self, data):

        def dfs(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = dfs(l)
            root.right = dfs(l)
            return root

        data_list = data.split(',')
        root = dfs(data_list)
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

ser = Codec()
deser = Codec()

serialized = ser.serialize(root)
print(serialized)
deserialized = deser.deserialize(serialized)

# Time: O(n)
# Space: O(n)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.idx = 0
        self.res = []
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for i in nestedList:
            if i.isInteger():
                self.res.append(i.getInteger())
            else:
                self.flatten(i.getList())

    def next(self) -> int:
        if self.hasNext():
            result = self.res[self.idx]
            self.idx += 1
            return result

    def hasNext(self) -> bool:
        return self.idx < len(self.res)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

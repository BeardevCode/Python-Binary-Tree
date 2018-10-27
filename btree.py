class Node:
    def __init__(self, value, level = 1):
        self.value = value
        self.count = 1
        self.level = level
        self.left = None
        self.right = None

    def Insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, self.level + 1)
                else:
                    self.left.Insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value, self.level + 1)
                else:
                    self.right.Insert(value)
            else:
                self.count += 1
        else:
            self.value = value

    # print the entire tree
    def PrintTree(self, allInfo):
        if self.left:
            self.left.PrintTree(allInfo)
        if allInfo is True:
            print("%d (Count = %d) - level %d" % (self.value, self.count, self.level))
        else:
            print(self.value)
        if self.right:
            self.right.PrintTree(allInfo)

    # print a level of the tree
    def PrintTreeLevel(self, lvl):
        if self.left:
            self.left.PrintTreeLevel(lvl)
        if self.level is lvl:
            print("%d (Count = %d) - level %d" % (self.value, self.count, self.level))
        if self.right:
            self.right.PrintTreeLevel(lvl)

# tests
root = Node(10)
root.Insert(6)
root.Insert(14)
root.Insert(3)
root.Insert(6)
root.Insert(1)
root.Insert(2)
root.Insert(6)
root.Insert(20)

root.PrintTree(False)

''' 
Output:
1
2
3
6
10
14
20
'''

root.PrintTree(True)

'''
Output:
1 (Count = 1) - level 4
2 (Count = 1) - level 5
3 (Count = 1) - level 3
6 (Count = 3) - level 2
10 (Count = 1) - level 1
14 (Count = 1) - level 2
20 (Count = 1) - level 3
'''

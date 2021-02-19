#!/bin/python3
from random import randint
from collections import deque
import timeit


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def __init__(self):
        self.q = list()
        self.real_q = deque()

    def levelOrder_ugly(self, root):
        # ugly as I do not want to use a list as a queue due to inefficiency
        if root is not None:
            print(root.data, end=" ")
        if root.left:
            self.q = [root.left] + self.q
        if root.right:
            self.q = [root.right] + self.q
        if len(self.q) > 0:
            self.levelOrder_ugly(self.q.pop())
        else:
            print("\n")

    def level_order_pythonic(self, root):
        if root is not None:
            print(root.data, end=" ")
        if root.left:
            self.real_q = [root.left] + self.q
        if root.right:
            self.real_q = [root.right] + self.q
        if len(self.real_q) > 0:
            self.levelOrder_ugly(self.real_q.pop())
        else:
            print("\n")


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


if __name__ == '__main__':
    T = []
    for i in range(100):
       T.append(randint(0, 10))
    myTree = Solution()
    root = None
    for i in T:
        root = myTree.insert(root, i)
    myTree.levelOrder_ugly(root)
    print("\n")
    myTree.level_order_pythonic(root)

    wrapped = wrapper(myTree.levelOrder_ugly, root)
    print("\n\n")
    res = timeit.timeit(wrapped, number=10)
    print(res)

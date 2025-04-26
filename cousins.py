from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 1. BFS - (using parent queue)
    # Approach: Level order traversal with extra parent queue to track parents separately.
    # TC: O(N), SC: O(N)
    def isCousins_BFS1(self, root, x, y):
        if not root:
            return False
        queue = deque()
        p_queue = deque()
        queue.append(root)
        p_queue.append(None)
        x_found = y_found = False
        x_parent = y_parent = None
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                parent = p_queue.popleft()
                if curr.val == x:
                    x_found, x_parent = True, parent
                if curr.val == y:
                    y_found, y_parent = True, parent
                if curr.left:
                    queue.append(curr.left)
                    p_queue.append(curr)
                if curr.right:
                    queue.append(curr.right)
                    p_queue.append(curr)
            if x_found and y_found:
                return x_parent != y_parent
            if x_found or y_found:
                return False
        return False

    # 2. BFS - Optimized (No Parent Queue)
    # Approach: Level order traversal, check for siblings while traversing.
    # TC: O(N), SC: O(N)
    def isCousins_BFS(self, root, x, y):
        if not root:
            return False
        queue = deque([root])
        while queue:
            x_found = y_found = False
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.val == x:
                    x_found = True
                if node.val == y:
                    y_found = True
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (
                        node.left.val == y and node.right.val == x
                    ):
                        return False  # siblings, not cousins
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if x_found and y_found:
                return True
            if x_found or y_found:
                return False
        return False

    # 3. DFS
    # Approach: Use DFS to track depth and parent for both x and y, then compare.
    # TC: O(N), SC: O(N)
    def isCousins_DFS(self, root, x, y):
        self.x_parent = self.y_parent = None
        self.x_depth = self.y_depth = -1

        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x:
                self.x_parent, self.x_depth = parent, depth
            if node.val == y:
                self.y_parent, self.y_depth = parent, depth
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)
        return self.x_depth == self.y_depth and self.x_parent != self.y_parent


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)


sol = Solution()
x, y = 4, 5

print(sol.isCousins_BFS1(root, x, y))  # Output: True
print(sol.isCousins_BFS(root, x, y))  # Output: True
print(sol.isCousins_DFS(root, x, y))  # Output: True

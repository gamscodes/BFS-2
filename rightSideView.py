from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS - Right First
    # Approach: Level order traversal, push right first, take first node at each level.
    # TC: O(N), SC: O(N)
    def rightSideView_BFS_RightFirst(self, root):
        if not root:
            return []
        queue, result = deque([root]), []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result

    # BFS - Left First
    # Approach: Level order traversal, push left first, take last node at each level.
    # TC: O(N), SC: O(N)
    def rightSideView_BFS_LeftFirst(self, root):
        if not root:
            return []
        queue, result = deque([root]), []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    # DFS - Right First
    # Approach: DFS, visit right first, record first node at each level.
    # TC: O(N), SC: O(N)
    def rightSideView_DFS_RightFirst(self, root):
        def dfs(node, level):
            if not node:
                return
            if len(result) == level:
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        result = []
        dfs(root, 0)
        return result

    # DFS - Left First
    # Approach: DFS, visit left first, overwrite node value at each level.
    # TC: O(N), SC: O(N)
    def rightSideView_DFS_LeftFirst(self, root):
        def dfs(node, level):
            if not node:
                return
            if len(result) <= level:
                result.append(node.val)
            else:
                result[level] = node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        result = []
        dfs(root, 0)
        return result


# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

sol = Solution()
print(sol.rightSideView_BFS_RightFirst(root))  # Output: [1,3,4]
print(sol.rightSideView_BFS_LeftFirst(root))  # Output: [1,3,4]
print(sol.rightSideView_DFS_RightFirst(root))  # Output: [1,3,4]
print(sol.rightSideView_DFS_LeftFirst(root))  # Output: [1,3,4]

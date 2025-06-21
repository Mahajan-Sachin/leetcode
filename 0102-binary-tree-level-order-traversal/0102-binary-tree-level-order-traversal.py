# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        que=deque()
        que.append(root)
        while que:
            level=[]
            for _ in range(len(que)):
                current=que.popleft()
                level.append(current.val)
                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)
            result.append(level)
        return result
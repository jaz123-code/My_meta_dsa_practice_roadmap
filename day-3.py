class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right



def maxDepth(root):
    if root is None:
        return 0
    if root.left is not None and root.right is None:
        return 1+maxDepth(root.left)
    if root.right is not None and root.left is None:
        return 1+maxDepth(root.right)
    return 1+max(maxDepth(root.left), maxDepth(root.right))

arr=[0,1,2,3,4,5,6,7,8,9,10]

def maxDepth2(root):
    if root is None:
        return 0
    return 1+max(maxDepth(root.left), maxDepth(root.right))

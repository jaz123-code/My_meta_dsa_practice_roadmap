#Not optimal approach O(n^2)
def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))

def isbalanced(root):
    if root is None:
        return True
    left=height(root.left)
    right=height(root.right)
    if abs(left-right)>1:
        return False
    return isbalanced(root.left) and isbalanced(root.right)

#Optimal approach O(n)
def checkHeight(root):
    if root is None:
        return 0
    left=checkHeight(root.left)
    if left==-1:
        return -1
    right=checkHeight(root.right)
    if right==-1:
        return -1
    if abs(left-right)>1:
        return -1
    return 1+max(left, right)
def isbalacned2(root):
    return checkHeight(root)!=-1

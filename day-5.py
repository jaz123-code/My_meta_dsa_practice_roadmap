
def find(node,p,q):
    if node is None:
        return None
    if node==p or node==q:
        return node
    left=find(node.left,p,q)
    right=find(node.right, p,q)
    if left and right:
        return node
    return left if left else right


    
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
def insert(root, data):
    if root is None:
        return TreeNode(data)
    curr = root 
    while True:
        if curr.data > data:
            if curr.left is None:
                curr.left = TreeNode(data)
                return root 
            curr = curr.left 
        else:
            if curr.right is None:
                curr.right = TreeNode(data)
                return root 
            curr = curr.right 
def bfs(root):
    stack = [root]
    cnt = 0
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        if node.left is None and node.right is None:
            cnt += 1
    return cnt
n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
print(bfs(tree))
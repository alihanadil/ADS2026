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
def dfs(root):
    stack = [root]
    cnt = 0
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        cnt += 1
    return cnt
n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
k = int(input())
curr = tree 
while curr.data != k:
    if curr.data < k:
        curr = curr.right 
    elif curr.data > k:
        curr = curr.left 
print(dfs(curr))
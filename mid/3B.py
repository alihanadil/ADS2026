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
        if curr.data == data:
            return root
        elif curr.data > data:
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
    stack = [(root, "new")]
    heights = {}
    while stack:
        node, state = stack.pop()
        if state == "new":
            stack.append((node, "ready"))
            if node.right:
                stack.append((node.right, "new"))
            if node.left:
                stack.append((node.left, "new"))
        else:
            lH = heights.get(node.left, 0)
            rH = heights.get(node.right, 0)
            heights[node] = 1 + max(lH, rH)
    return heights[root]
n = int(input())
tree = None 
for i in map(int, input().split()):
    tree = insert(tree, i)
print(dfs(tree))
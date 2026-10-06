class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None
def insert(root, data):
    if root is None:
        return TreeNode(data)
    cur = root 
    while True:
        if data == cur.data:
            return root
        elif data < cur.data:
            if cur.left is None:
                cur.left = TreeNode(data)
                return root
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(data)
                return root
            cur = cur.right

def dfs(root):
    if root is None:
        return None 
    stack = [(root, "new")]
    heights = {}
    best = 0
    while stack:
        node, state = stack.pop()
        if state == "new":
            stack.append((node, "ready"))
            if node.right:
                stack.append((node.right, "new"))
            if node.left:
                stack.append((node.left, "new"))
        else:
            leftH = heights.get(node.left, 0)
            rightH = heights.get(node.right, 0)
            heights[node] = 1 + max(leftH, rightH)
            best = max(best, leftH + rightH + 1)
    return best 
n = int(input())
tree = None 
for i in map(int, input().split()):
    tree = insert(tree, i)
print(dfs(tree))